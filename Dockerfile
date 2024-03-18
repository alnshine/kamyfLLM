# Используем базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости проекта в контейнер
COPY . .

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir \
    altgraph==0.17.2 \
    annotated-types==0.6.0 \
    appnope==0.1.4 \
    asttokens==2.4.1 \
    attrs==23.2.0 \
    beautifulsoup4==4.12.3 \
    bleach==6.1.0 \
    blinker==1.7.0 \
    cachetools==5.3.3 \
    certifi==2024.2.2 \
    chardet==3.0.4 \
    charset-normalizer==3.3.2 \
    click==8.1.7 \
    decorator==5.1.1 \
    defusedxml==0.7.1 \
    entrypoints==0.4 \
    exceptiongroup==1.2.0 \
    executing==2.0.1 \
    fastjsonschema==2.19.1 \
    Flask==3.0.2 \
    future==0.18.2 \
    google-ai-generativelanguage==0.4.0 \
    google-api-core==2.17.1 \
    google-auth==2.28.2 \
    google-cloud-aiplatform==1.44.0 \
    google-cloud-bigquery==3.19.0 \
    google-cloud-core==2.4.1 \
    google-cloud-resource-manager==1.12.3 \
    google-cloud-storage==2.15.0 \
    google-crc32c==1.5.0 \
    google-generativeai==0.4.1 \
    google-resumable-media==2.7.0 \
    googleapis-common-protos==1.63.0 \
    grpc-google-iam-v1==0.13.0 \
    grpcio==1.62.1 \
    grpcio-status==1.62.1 \
    idna==2.8 \
    importlib_metadata==7.0.2 \
    ipykernel==4.6.1 \
    ipython==5.5.0 \
    ipython-genutils==0.2.0 \
    itsdangerous==2.1.2 \
    jedi==0.19.1 \
    Jinja2==3.1.3 \
    jsonschema==4.21.1 \
    jsonschema-specifications==2023.12.1 \
    jupyter-client==7.1.2 \
    jupyter_core==5.7.2 \
    jupyterlab_pygments==0.3.0 \
    macholib==1.15.2 \
    MarkupSafe==2.1.5 \
    matplotlib-inline==0.1.6 \
    mistune==3.0.2 \
    nbclient==0.10.0 \
    nbconvert==7.16.2 \
    nbformat==5.10.3 \
    nest-asyncio==1.6.0 \
    numpy==1.26.4 \
    packaging==24.0 \
    pandocfilters==1.5.1 \
    parso==0.8.3 \
    pexpect==4.9.0 \
    pickleshare==0.7.5 \
    platformdirs==4.2.0 \
    portpicker==1.2.0 \
    prompt-toolkit==1.0.18 \
    proto-plus==1.23.0 \
    protobuf==4.25.3 \
    ptyprocess==0.7.0 \
    pure-eval==0.2.2 \
    pyasn1==0.5.1 \
    pyasn1-modules==0.3.0 \
    pydantic==2.6.4 \
    pydantic_core==2.16.3 \
    Pygments==2.17.2 \
    python-dateutil==2.9.0.post0 \
    python-dotenv==1.0.1 \
    pytz==2024.1 \
    pyzmq==25.1.2 \
    referencing==0.34.0 \
    requests==2.21.0 \
    rpds-py==0.18.0 \
    rsa==4.9 \
    shapely==2.0.3 \
    simplegeneric==0.8.1 \
    six==1.12.0 \
    soupsieve==2.5 \
    stack-data==0.6.3 \
    terminado==0.13.3 \
    tinycss2==1.2.1 \
    tornado==4.5.3 \
    tqdm==4.66.2 \
    traitlets==5.14.2 \
    typing_extensions==4.10.0 \
    urllib3==1.24.3 \
    vertexai==1.43.0 \
    wcwidth==0.2.13 \
    webencodings==0.5.1 \
    Werkzeug==3.0.1 \
    zipp==3.18.1

# Определяем переменную окружения для Flask
ENV FLASK_APP=main.py

# Открываем порт, который будет использоваться Flask приложением
EXPOSE 8080

# Запускаем Flask приложение при старте контейнера
CMD ["flask", "run", "--host=0.0.0.0"]
