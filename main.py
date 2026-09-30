from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return{"mensagem":"it's over meus bacanos, perdi no xadrez para a mosca da fruta"}


