#!/bin/bash

GPU_ID=0,1,2,3,4,5,6,7

# Set CUDA to use the specified GPU
export CUDA_VISIBLE_DEVICES=$GPU_ID

# 定义模型名称到模型路径的映射
declare -A model_paths
model_paths["model_name"]=model_path

# Loop through each model and run zeroshot and fewshot
for model_name in "${!model_paths[@]}"; do
    echo ">>> Running fewshot for $model_name"
    lm_eval \
        --model hf \
        --model_args pretrained=${model_paths[$model_name]},trust_remote_code=True,parallelize=True \
        --include_path ./ \
        --tasks cmoraleval \
        --output ./output/$model_name/fewshot \
        --log_samples \
        --batch_size 8 \ #可根据计算资源自行修改
        --num_fewshot 5 
done