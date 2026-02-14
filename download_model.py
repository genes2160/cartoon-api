from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="akhaliq/AnimeGANv2",
    filename="paprika.onnx",
    local_dir="models",
    local_dir_use_symlinks=False
)

print("Downloaded to:", path)
