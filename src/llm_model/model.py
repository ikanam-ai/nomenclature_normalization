import fire
from llama_cpp import Llama

class Model:
    def __init__(self, model_path='model-q4_K.gguf', n_ctx=2000, top_k=30, top_p=0.9, temperature=0, repeat_penalty=1.1):
        self.SYSTEM_PROMPT = "" #"Ты — Сайга, русскоязычный автоматический ассистент. Ты разговариваешь с людьми и помогаешь им."
        self.model = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_parts=1,
            n_gpu_layers=-1
        )
        self.top_k = top_k
        self.top_p = top_p
        self.temperature = temperature
        self.repeat_penalty = repeat_penalty

    def get_message_tokens(self, role, content):
        content = f"{role}\n{content}\n</s>"
        content = content.encode("utf-8")
        message_tokens = self.model.tokenize(content, special=True)
        return message_tokens

    def get_system_tokens(self):
        system_message = {
            "role": "system",
            "content": self.SYSTEM_PROMPT
        }
        return self.get_message_tokens(**system_message)

    def interact(self, user_message):
        system_tokens = self.get_system_tokens()
        tokens = system_tokens
        self.model.eval(tokens)

        message_tokens = self.get_message_tokens(role="user", content=user_message)
        role_tokens = self.model.tokenize("bot\n".encode("utf-8"), special=True)
        tokens += message_tokens + role_tokens
        full_prompt = self.model.detokenize(tokens)
        generator = self.model.generate(
            tokens,
            top_k=self.top_k,
            top_p=self.top_p,
            temp=self.temperature,
            repeat_penalty=self.repeat_penalty
        )
        token_str = ''
        for token in generator:
            token_str += self.model.detokenize([token]).decode("utf-8", errors="ignore")
            tokens.append(token)
            if token == self.model.token_eos():
                break
        return token_str
