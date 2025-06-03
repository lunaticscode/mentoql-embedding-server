from fastapi import Request, HTTPException, Depends
import jwt
from utils.config import AppConfig
from utils.logger import log_error
auth_err_msg_for_user = "(!) Authentication failed"
def auth_middleware():
    def _inner(request: Request):
        try:
            token = request.headers.get("Authorization")
            payload = jwt.decode(token, AppConfig.JWT_SECRET, algorithms=AppConfig.JWT_ALGORITHM)
            return payload
        except jwt.ExpiredSignatureError:
            log_error("auth_middleware :: jwt.ExpiredSignatureError")
            raise HTTPException(status_code=401, detail=auth_err_msg_for_user)
        except jwt.InvalidTokenError:
            log_error("auth_middleware :: jwt.InvalidTokenError")
            raise HTTPException(status_code=401, detail=auth_err_msg_for_user)
        except jwt.PyJWTError:
            log_error("auth_middleware :: jwt.PyJWTError")
            raise HTTPException(status_code=401, detail=auth_err_msg_for_user)
        except Exception as e:
            log_error("auth_middleware :: Exception Error")
            raise HTTPException(status_code=500, detail="(!) SERVER_ERROR")
    return Depends(_inner)




