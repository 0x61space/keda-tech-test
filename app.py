from typing import Any, Dict

from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(
    event: Dict, 
    context: LambdaContext,
) -> Dict[str, Any]:
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '{"message": "Hello from Python 3.13!"}'
    }
