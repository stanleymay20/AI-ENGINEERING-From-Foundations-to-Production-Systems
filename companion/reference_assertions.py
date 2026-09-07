"""Deterministic regression tests for the book's reference-tested examples.

These tests intentionally avoid network access and optional services. Their purpose is to
catch accidental changes to numerical results printed in the study edition.
"""
from __future__ import annotations

import math
import tempfile
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.datasets import load_iris, make_blobs, make_classification
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    davies_bouldin_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
    silhouette_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def close(actual: float, expected: float, tol: float = 1e-6) -> None:
    assert abs(actual - expected) <= tol, (actual, expected)


def ch2_python_numpy_pandas() -> None:
    raw = [10.5, 12.1, 8.9, 15.0, 11.7]
    lo, hi = min(raw), max(raw)
    norm = [(x - lo) / (hi - lo) for x in raw]
    assert np.allclose(
        norm,
        [0.2622950819672131, 0.5245901639344261, 0.0, 1.0, 0.4590163934426228],
    )
    matrix = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
    assert matrix[1, 2] == 70
    rng = np.random.default_rng(42)
    close(float(rng.random((4, 3))[0, 0]), 0.7739560485559633)


def ch4_eda() -> None:
    rng = np.random.default_rng(42)
    n = 100
    experience = rng.integers(0, 40, n)
    age = np.clip(22 + experience + rng.normal(0, 6, n), 18, 70).round().astype(int)
    education = rng.choice(
        ["High School", "Bachelor", "Master", "PhD"],
        n,
        p=[0.30, 0.40, 0.20, 0.10],
    )
    bonus = pd.Series(education).map(
        {"High School": 0, "Bachelor": 5000, "Master": 10000, "PhD": 15000}
    ).to_numpy()
    salary = 30000 + 1200 * experience + bonus + rng.normal(0, 8000, n)
    df = pd.DataFrame({"Age": age, "Salary": salary, "Experience": experience})
    df.loc[0, "Salary"] = 200000
    df.loc[5, "Age"] = 95
    close(float(df["Salary"].mean()), 62461.032838, 1e-3)
    close(float(df["Salary"].skew()), 2.779501, 1e-6)
    close(float(df.corr().loc["Age", "Experience"]), 0.853, 5e-4)


def ch5_examples() -> None:
    np.random.seed(42)
    sizes = 500 + 150 * np.random.randn(100, 1)
    prices = 100000 + 50 * sizes + 10000 * np.random.randn(100, 1)
    sizes = np.maximum(sizes, 500)
    prices = np.maximum(prices, 50000)
    xtr, xte, ytr, yte = train_test_split(sizes, prices, test_size=0.2, random_state=42)
    model = LinearRegression().fit(xtr, ytr)
    close(float(model.intercept_[0]), 78019.7989, 1e-2)
    close(float(model.coef_[0][0]), 84.7497, 1e-2)

    iris = load_iris()
    xtr, xte, ytr, yte = train_test_split(
        iris.data, iris.target, test_size=0.30, random_state=42, stratify=iris.target
    )
    knn = KNeighborsClassifier(n_neighbors=3).fit(xtr, ytr)
    close(float(accuracy_score(yte, knn.predict(xte))), 0.9555555556, 1e-9)


def ch6_regression() -> None:
    np.random.seed(42)
    n = 100
    experience = np.random.rand(n) * 10
    education = np.random.randint(0, 4, n)
    X = pd.DataFrame({"Experience": experience, "Education_Level": education})
    y = 25000 + 3000 * X["Experience"] + 5000 * X["Education_Level"] + np.random.randn(n) * 5000
    xtr, xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(xtr, ytr)
    pred = model.predict(xte)
    close(float(model.intercept_), 25449.25, 0.01)
    assert np.allclose(model.coef_, [3053.178332, 5058.462248], atol=1e-6)
    close(float(mean_absolute_error(yte, pred)), 3654.58, 0.01)
    close(float(math.sqrt(mean_squared_error(yte, pred))), 4500.30, 0.01)
    close(float(r2_score(yte, pred)), 0.8319, 5e-5)


def ch7_classifiers() -> None:
    X, y = make_classification(
        n_samples=200,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_classes=2,
        random_state=42,
    )
    xtr, xte, ytr, yte = train_test_split(X, y, test_size=0.30, random_state=42)
    scaler = StandardScaler()
    xtr = scaler.fit_transform(xtr)
    xte = scaler.transform(xte)
    specs = [
        (LogisticRegression(random_state=42), (0.8333, 0.8000, 0.8571, 0.8276, 0.9085)),
        (KNeighborsClassifier(n_neighbors=5), (0.8333, 0.8214, 0.8214, 0.8214, 0.9007)),
        (SVC(kernel="rbf", random_state=42, probability=True), (0.8167, 0.7931, 0.8214, 0.8070, 0.9096)),
    ]
    for model, expected in specs:
        model.fit(xtr, ytr)
        pred = model.predict(xte)
        prob = model.predict_proba(xte)[:, 1]
        actual = (
            accuracy_score(yte, pred),
            precision_score(yte, pred),
            recall_score(yte, pred),
            f1_score(yte, pred),
            roc_auc_score(yte, prob),
        )
        assert np.allclose(actual, expected, atol=5e-5), (actual, expected)


def ch8_ensembles() -> None:
    X, y = make_classification(
        n_samples=380, n_features=8, n_informative=5, n_redundant=1, random_state=42
    )
    xtr, xte, ytr, yte = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
    tree = DecisionTreeClassifier(max_depth=4, random_state=42).fit(xtr, ytr)
    forest = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=42).fit(xtr, ytr)
    boost = GradientBoostingClassifier(random_state=42).fit(xtr, ytr)
    assert 0 <= tree.score(xte, yte) <= 1
    assert 0 <= forest.oob_score_ <= 1
    assert boost.score(xte, yte) >= 0.75


def ch9_clustering() -> None:
    X, _ = make_blobs(n_samples=300, centers=4, n_features=2, cluster_std=1.0, random_state=42)
    X = StandardScaler().fit_transform(X)
    km = KMeans(n_clusters=4, n_init=10, random_state=42).fit(X)
    ag = AgglomerativeClustering(n_clusters=4).fit(X)
    close(float(silhouette_score(X, km.labels_)), 0.7974739889632732, 1e-12)
    close(float(davies_bouldin_score(X, km.labels_)), 0.2811066469065262, 1e-12)
    close(float(silhouette_score(X, ag.labels_)), 0.7974739889632732, 1e-12)


def ch11_forward() -> None:
    X = np.array([[0.6, 0.1]])
    W1 = np.array([[0.5, -0.3], [0.8, 0.2]])
    b1 = np.array([0.1, -0.1])
    W2 = np.array([[0.7], [-0.4]])
    hidden = np.maximum(0, X @ W1 + b1)
    out = hidden @ W2 + np.array([0.05])
    assert np.allclose(hidden, [[0.48, 0.0]])
    close(float(out[0, 0]), 0.386, 1e-12)


def ch17_recommender() -> None:
    df = pd.DataFrame(
        {
            "UserID": [1,1,1,2,2,2,3,3,3,1,2,3],
            "MovieID": [101,102,103,101,103,104,102,105,101,104,105,103],
            "Rating": [4.,5.,3.,5.,4.,2.,4.,5.,3.,2.,5.,4.],
        }
    )
    mat = df.pivot_table(index="MovieID", columns="UserID", values="Rating").fillna(0)
    from sklearn.metrics.pairwise import cosine_similarity
    sim = pd.DataFrame(cosine_similarity(mat), index=mat.index, columns=mat.index)
    close(float(sim.loc[101, 103]), 0.971797, 1e-6)
    close(float(sim.loc[103, 105]), 0.883452, 1e-6)


def ch18_q_learning() -> None:
    start, pit, goal = 0, 4, 8
    Q = np.zeros((9, 4))
    alpha, gamma, epsilon = 0.2, 0.9, 0.2
    rng = np.random.default_rng(42)

    def step(state: int, action: int):
        row, col = divmod(state, 3)
        dr, dc = [(-1,0), (0,1), (1,0), (0,-1)][action]
        nr, nc = min(max(row + dr, 0), 2), min(max(col + dc, 0), 2)
        nxt = nr * 3 + nc
        if nxt == goal:
            return nxt, 10.0, True
        if nxt == pit:
            return nxt, -10.0, True
        return nxt, -0.1, False

    for _ in range(3000):
        state, done = start, False
        while not done:
            action = int(rng.integers(4)) if rng.random() < epsilon else int(np.argmax(Q[state]))
            nxt, reward, done = step(state, action)
            target = reward if done else reward + gamma * np.max(Q[nxt])
            Q[state, action] += alpha * (target - Q[state, action])
            state = nxt
    assert int(np.argmax(Q[start])) == 1
    assert np.allclose(np.round(Q[start], 3), [6.217, 7.019, 7.019, 6.217])


def ch23_serialization() -> None:
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    xtr, xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression().fit(xtr, ytr)
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "model.joblib"
        joblib.dump(model, path)
        loaded = joblib.load(path)
        close(float(loaded.score(xte, yte)), 1.0)


def ch24_psi() -> None:
    def psi(reference, current, bins=10):
        edges = np.quantile(reference, np.linspace(0, 1, bins + 1))
        edges[0], edges[-1] = -np.inf, np.inf
        rc, _ = np.histogram(reference, bins=edges)
        cc, _ = np.histogram(current, bins=edges)
        rp = np.clip(rc / rc.sum(), 1e-6, None)
        cp = np.clip(cc / cc.sum(), 1e-6, None)
        return float(np.sum((cp - rp) * np.log(cp / rp)))

    rng = np.random.default_rng(42)
    reference = rng.normal(40, 10, 5000)
    current = rng.normal(44, 11, 5000)
    close(psi(reference, current), 0.1676, 5e-5)


def main() -> None:
    tests = [
        ch2_python_numpy_pandas,
        ch4_eda,
        ch5_examples,
        ch6_regression,
        ch7_classifiers,
        ch8_ensembles,
        ch9_clustering,
        ch11_forward,
        ch17_recommender,
        ch18_q_learning,
        ch23_serialization,
        ch24_psi,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"ALL PASS: {len(tests)} deterministic reference groups")


if __name__ == "__main__":
    main()
