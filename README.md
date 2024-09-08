# Autocrawling Agent
Auto crawling content of website using GPT-4O vision api.
```
!!! Due to limitation of performance, crawling result can be different compared to original website content. !!!
```
## How to use
1. make ".env" file. ".env" file must have "OPENAI_API_KEY" information.
    ```shell
    cd autocrawling_agent
    vi .env
    ...    
    ```
2. build docker image
    ```shell
    docker build -t autocrawling_agent_image .
    ```
3. run docker container
    ```shell
    docker run -itd -p 8000:8000 --name autocrawling_agent_api_container autocrawling_agent_image
    ```
4. start uvicorn server
    ```shell
    docker exec -it autocrawling_agent_api_container bash
    ...
    cd /workspace
    uvicorn src.api.main:app --port 8000
    ```
