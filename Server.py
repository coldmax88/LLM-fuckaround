import socket
from transformers import AutoTokenizer, GemmaForCausalLM,LlamaForCausalLM
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoModel, AutoTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer

import torch
import subprocess
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

torch.cuda.empty_cache()
model3_2="mistralai/Mixtral-8x7B-Instruct-v0.1"
model3_1="mistralai/Mistral-7B-Instruct-v0.2"

model2_4="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
model2_3="meta-llama/Llama-2-70b-hf"
model2_2="meta-llama/Llama-2-13b-hf"
model2_1="meta-llama/Llama-2-7b-hf"
model2_0="CodeLlama-7B-Instruct-GGUF"


model1_22="google/gemma-7b"
model1_12="google/gemma-2b"

model1_21="google/gemma-7b-it"
model1_11="google/gemma-2b-it"

model=model3_2
#quantization_config = BitsAndBytesConfig(load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained(model,token="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")
model = AutoModelForCausalLM.from_pretrained(model,token="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")#, quantization_config=quantization_config)

try:
    subprocess.check_output('nvidia-smi')
    model.to("cuda")
    print(1)
    Gpu=True
    torch.cuda.empty_cache()
except:
  model.to("cpu")
  print(2)
  Gpu=False

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('203.0.40.50', 12345))
    server_socket.listen(1)
    print("Server gestartet und hört auf Port 12345")
    i=0
    while True:
        client_socket, addr = server_socket.accept()
        #print(f"Verbindung von {addr} akzeptiert")

        data = client_socket.recv(1024).decode()
        #print(f"Vom Client empfangene Frage: {data}")


        input_text = str(data)
        if Gpu==True:
            input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")
        else:
            input_ids = tokenizer(input_text, return_tensors="pt")
        
        
        outputs = model.generate(**input_ids,max_length=300000)#, temperature=0.7)
        output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        
        output_lines = output_text.split('. ')
        
        
        answer = output_lines
        client_socket.send(answer.encode())
        print("Tick",i)
        i=i+1
        client_socket.close()

if __name__ == "__main__":
    start_server()
