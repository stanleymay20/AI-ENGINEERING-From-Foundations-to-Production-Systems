"""Chapter 8 exercise reference: bagging vs boosting on California Housing."""
from __future__ import annotations

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def main() -> None:
    X, y = fetch_california_housing(return_X_y=True, as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    models = {
        "RandomForest": RandomForestRegressor(
            n_estimators=250,
            min_samples_leaf=2,
            n_jobs=-1,
            random_state=42,
        ),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, pred)
        rmse = mean_squared_error(y_test, pred) ** 0.5
        print(f"{name:16s} MAE={mae:.4f} RMSE={rmse:.4f}")


if __name__ == "__main__":
    main()
