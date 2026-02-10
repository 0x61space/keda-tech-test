FROM public.ecr.aws/lambda/python:3.13

COPY requirements/ ${LAMBDA_TASK_ROOT}/requirements/
RUN pip install --no-cache-dir -r requirements/prod.txt

COPY app.py ${LAMBDA_TASK_ROOT}

CMD [ "app.lambda_handler" ]
