import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "app_fastapi:app",
        host='localhost',
        # host='0.0.0.0',
        port=8000,
        reload=True,
    )
