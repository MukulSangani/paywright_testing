import requests
import json


def getAuthToken():
    url = 'http://adobev2.qmigrator.ai/api/v1/Sec/VerifywithEmail'
    headers = {'content-type': 'application/json'}
    body = {
        "content": "s72ujtSylYOK3+JZ7vlcF7OVIxRoINwCnFiSzZiN4mPbaZYSon9r3zCOCQjSt6tZY5wXJ481PGTqoDvlCmExsmW5IeWxQTN7yiasrRYfOtaMMIx4LS+WOi7TlFB64Cc2/ywlnFnIJe+bvRVAdCAagGxx0FHKaNNDyWWaqGezII6cmT/DT6grMd9jJkhCOjmLJ4cJdoWrd7tqrOdVo7kN04DyPhas4it3N/AbXdua20eECr592CZ3EGb+dkG1+ko6",
        "signContent": "DN3Brk+mwM/AC04aspYrTwh+jTMkw7z0BChXYc5NKhzyI85XR3PJXUf/Hs+eefz8dfBkqPz4iaMcGKPctIUGTgbHLlHuc8Rcy62oGoSApMpkZQj13SyBOfgUvKTzkHBkMD4ZA++HHBomBi05Cb1uVgxl5wEupWPOV38y8//nuwU=",
        "email": "sunil.kamuju@quadranttechnologies.com"
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    if not response.ok:
        raise Exception('Failed to fetch token')
    data = response.json()
    return data['token']


def test_api_get_request():
    response = requests.get('http://adobev2.qmigrator.ai/')
    assert response.status_code == 200
    print('login api :', response.status_code)


def test_api_get_filexist_request():
    headers = {'content-type': 'application/json'}
    data = {
        "content": "s72ujtSylYOK3+JZ7vlcF7OVIxRoINwCnFiSzZiN4mPbaZYSon9r3zCOCQjSt6tZY5wXJ481PGTqoDvlCmExsmW5IeWxQTN7yiasrRYfOtaMMIx4LS+WOi7TlFB64Cc2/ywlnFnIJe+bvRVAdCAagGxx0FHKaNNDyWWaqGezII6cmT/DT6grMd9jJkhCOjmLJ4cJdoWrd7tqrOdVo7kN04DyPhas4it3N/AbXdua20eECr592CZ3EGb+dkG1+ko6",
        "signContent": "DN3Brk+mwM/AC04aspYrTwh+jTMkw7z0BChXYc5NKhzyI85XR3PJXUf/Hs+eefz8dfBkqPz4iaMcGKPctIUGTgbHLlHuc8Rcy62oGoSApMpkZQj13SyBOfgUvKTzkHBkMD4ZA++HHBomBi05Cb1uVgxl5wEupWPOV38y8//nuwU=",
        "email": "sunil.kamuju@quadranttechnologies.com"
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Sec/fileExist', headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    print('login api2 :', response.status_code)


def test_api_post_verifyemail_request():
    data = {
        "content": "s72ujtSylYOK3+JZ7vlcF7OVIxRoINwCnFiSzZiN4mPbaZYSon9r3zCOCQjSt6tZY5wXJ481PGTqoDvlCmExsmW5IeWxQTN7yiasrRYfOtaMMIx4LS+WOi7TlFB64Cc2/ywlnFnIJe+bvRVAdCAagGxx0FHKaNNDyWWaqGezII6cmT/DT6grMd9jJkhCOjmLJ4cJdoWrd7tqrOdVo7kN04DyPhas4it3N/AbXdua20eECr592CZ3EGb+dkG1+ko6",
        "email": "sunil.kamuju@quadranttechnologies.com",
        "signContent": "DN3Brk+mwM/AC04aspYrTwh+jTMkw7z0BChXYc5NKhzyI85XR3PJXUf/Hs+eefz8dfBkqPz4iaMcGKPctIUGTgbHLlHuc8Rcy62oGoSApMpkZQj13SyBOfgUvKTzkHBkMD4ZA++HHBomBi05Cb1uVgxl5wEupWPOV38y8//nuwU="
    }
    response = requests.post('http://adobev2.qmigrator.ai/api/v1/Sec/VerifywithEmail', data=json.dumps(data))
    assert response.status_code == 200
    print("login api3: ", response.status_code)


def test_get_projectmenu_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetSecUserProjectMenu?projectId=1167',
                            headers=headers)
    assert response.status_code == 200
    print("login api4: ", response.status_code)


def test_get_connectionlist_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
                            headers=headers)
    assert response.status_code == 200
    print("Login api5: ", response.status_code)


def test_post_getdata(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
                            headers=headers)
    assert response.status_code == 200
    print("login api6: ", response.status_code)


def test_get_commanfilesfromdirectoryapi(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetCommonFilesFromDirectory?path=PRJ1167SRC/undefined/Reports/Object_Count_Reports/',
        headers=headers)

    assert response.status_code == 204
    print(' assessment api assessment1: ', response.status_code)


def test_get_connectionlist_Assessment_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
                            headers=headers)

    assert response.status_code == 200
    print(' assessment api assessment2: ', response.status_code)


def test_get_rwquesttabledata_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Extraction',
        headers=headers)

    assert response.status_code == 200
    print(' assessment api assessment3: ', response.status_code)


def test_get_requesttabledata_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Extraction',
        headers=headers)

    assert response.status_code == 200
    print(' assessment api assessment4: ', response.status_code)


def test_get_operationlist_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetOperationList?projectId=1167&OperationType=Extraction',
        headers=headers)

    assert response.status_code == 200
    print(' assessment api assessment5 ', response.status_code)


def test_post_individuallogs_api(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    data = {
        "projectId": "1167",
        "operationType": "Extraction",
        "action": "null",
        "row_id": "null",
        "runno": "null",
        "operationName": "null"
    }
    response = requests.post('http://adobev2.qmigrator.ai/api/v1/Project/GetIndividualLogs', headers=headers,
                             data=json.dumps(data))

    assert response.status_code == 200
    print(' assessment api assessment6: ', response.status_code)


def test_get_getcommanfilesfromdirectory_codescan(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetCommonFilesFromDirectory?path=PRJ1167SRC//Reports/Assessment_Reports/',
        headers=headers)

    assert response.status_code == 204
    print(' assessment api codescan1: ', response.status_code)


def test_get_getconnectionlist_codescan(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
                            headers=headers)
    assert response.status_code == 200
    print(' assessment api codescan2: ', response.status_code)


def test_get_getrequesttabledata_codescan(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Assessment',
        headers=headers)

    assert response.status_code == 200
    print(' assessment api codescan3: ', response.status_code)


def test_get_getoperationlist_codescan(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetOperationList?projectId=1167&OperationType=Assessment',
        headers=headers)

    assert response.status_code == 200
    print(' assessment api codescan4: ', response.status_code)


def test_get_getindividuallogs_codescan(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    data = {
        "projectId": "1167",
        "operationType": "Assessment",
        "operationName": "null",
        "action": "null",
        "row_id": "null",
        "runno": "null"
    }
    response = requests.post('http://adobev2.qmigrator.ai/api/v1/Project/GetIndividualLogs', headers=headers,
                             data=json.dumps(data))

    assert response.status_code == 200
    print(' assessment api codescan5: ', response.status_code)


def test_get_getrunnumbers_codescan(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetRunNumbers?projectId=1167', headers=headers)

    assert response.status_code == 200
    print(' assessment api codescan6: ', response.status_code)


token = getAuthToken()
# getAuthToken()
test_api_get_request()
test_api_get_filexist_request()
test_get_projectmenu_api(token)
test_get_connectionlist_api(token)
test_post_getdata(token)
test_get_commanfilesfromdirectoryapi(token)
test_get_connectionlist_Assessment_api(token)
test_get_rwquesttabledata_api(token)
test_get_requesttabledata_api(token)
test_get_operationlist_api(token)
test_post_individuallogs_api(token)
test_get_getcommanfilesfromdirectory_codescan(token)
test_get_getconnectionlist_codescan(token)
test_get_getrequesttabledata_codescan(token)
test_get_getoperationlist_codescan(token)
test_get_getindividuallogs_codescan(token)
test_get_getrunnumbers_codescan(token)
