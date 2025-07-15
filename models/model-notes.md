# Model Training Notes

## Validation Accuracy: `train0`  
*Note: "v1" = IMAGENET1K_V1, "v2" = V2*
*Accuracy numbers didn't meet my standards*

| Model         | Run 0    |
|---------------|----------|
| ResNet50 v1   | 0.764273 |
| ResNet50 v2   | 0.729282 |
| ResNet101 v1  | 0.775936 |
| ResNet101 v2  | 0.790055 |

---

## Validation Accuracy: `train1`  
*Utilizes new labeled test set from Stanford Cars for more data!*

| Model         | Run 0    |
|---------------|----------|
| ResNet50 v1   | 0.848023 |
| ResNet50 v2   | 0.833607 |
| ResNet101 v1  | **0.867381** |
| ResNet101 v2  | 0.861614 |

---

## Hyperparameterization: ResNet101v1 (`train1` best model)  
*Hyperparameters changed: optimizer and learning rate*

| Description    | Run 0     |
|----------------|-----------|
| Adam, lr=1e-4  | **0.867381** (baseline) ⭐ |
| Adam, lr=3e-4  | 0.717875  |
| Adam, lr=5e-5  | 0.841050  |
| SGD, lr=1e-2   | 0.691104  |
| SGD, lr=5e-3   | 0.417627  |

---

## Observations & Conclusions

- **More data improves accuracy:** All models saw substantial gains in `train1` compared to `train0`.
- **Deeper models help:** ResNet101 generally outperforms ResNet50.
- **Optimizer matters:** Adam (`lr=1e-4`) yielded the highest accuracy; both lower/higher learning rates and SGD performed worse.
- **IMAGENET v1 vs v2:** The difference between v1 and v2 initializations is minor compared to the effect of data volume and model size.
- **Performance margins:** The right optimizer and learning rate can more than double validation accuracy for the same architecture.
