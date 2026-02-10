FROM public.ecr.aws/lambda/python:3.13

# Copy requirements and install dependencies
COPY requirements/dev.txt ${LAMBDA_TASK_ROOT}
RUN pip install --no-cache-dir -r requirements.txt

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "app.lambda_handler" ]
