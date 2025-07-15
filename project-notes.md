# Training Notes

**validation accuracy results from train0**
note: "v1" is IMAGENET1K_V1, "v2" is V2

model,           run0
resnet50v1,      0.764273
resnet50v2,      0.729282
resnet101v1,     0.775936
resnet101v2,     0.790055

**validation accuracy results from train1**
utilizes new labeled test set from Stanford Cars for more data!

model,           run0
resnet50v1,      0.848023
resnet50v2,      0.833607
resnet101v1,     0.867381  **
resnet101v2,     0.861614

**hyperparameterization of resnet101v1 model** (best performance from train1)
hyperparameters changed were from the optimizer

description,     run0
adam_lr1e-4,     0.867381  **(baseline performance from train1)
adam_lr3e-4,     0.717875
adam_lr5e-5,     0.841050
sgd_lr1e-2,      0.691104
sgd_lr5e-3,      0.417627

**Observations & Conclusions:**
 - 