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


def test_get_connectionList(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
                            headers=headers)
    assert response.status_code == 200
    print(" code migration api1 SO: ", response.status_code)


def test_get_objectType_storageobject(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetObjectTypes?projectId=1167&objectgroupname=Storage_Objects',
        headers=headers)
    assert response.status_code == 200
    print(" code migration api2 SO: ", response.status_code)


def test_get_runNumbers_storageobject(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get('http://adobev2.qmigrator.ai/api/v1/Project/GetRunNumbers?projectId=1167',
                            headers=headers)
    assert response.status_code == 200
    print(" code migration api3 SO: ", response.status_code)


def test_post_individualLogs_storageobject(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    data = {

        "projectId": "1167",
        "operationType": "Conversion",
        "operationName": "Storage_Objects",
        "action": "null",
        "row_id": "null",
        "runno": "null"

    }
    response = requests.post('http://adobev2.qmigrator.ai/api/v1/Project/GetIndividualLogs',
                             headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    print(" code migration api4 SO: ", response.status_code)


def test_get_requestTbaledata_storageobject(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Conversion',
        headers=headers)
    assert response.status_code == 200
    print(" code migration api5 SO: ", response.status_code)


def test_get_reportValidation_storageobject(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetFilesFromDirectory?path=PRJ1167SRC/undefined/Reports/Validation_Reports/Storage_Objects/',
        headers=headers)
    # print(response)
    assert response.status_code == 204
    print(" code migration api6 SO: ", response.status_code)


def test_get_connectionList_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api1 CO: ", response.status_code)


def test_get_objectTypes_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetObjectTypes?projectId=1167&objectgroupname=Code_Objects',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api2 CO: ", response.status_code)


def test_get_runNumbers_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRunNumbers?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api3 CO: ", response.status_code)


def test_get_runNumbers_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRunNumbers?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api3 CO: ", response.status_code)


def test_post_individualLogs_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    data = {
        "projectId": "1167",
        "operationType": "Conversion",
        "operationName": "Code_Objects",
        "action": "null",
        "row_id": "null",
        "runno": "null"
    }
    response = requests.post(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetIndividualLogs',
        headers=headers, data=json.dumps(data))
    # print(response)
    assert response.status_code == 200
    print(" code migration api4 CO: ", response.status_code)


def test_get_requestTabledata_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Conversion',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api5 CO: ", response.status_code)


def test_get_reportvalidation_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetFilesFromDirectory?path=PRJ1167SRC/undefined/Reports/Validation_Reports/Code_Objects/',
        headers=headers)
    # print(response)
    assert response.status_code == 204
    print(" code migration api6 CO: ", response.status_code)


def test_get_requestTabledata1_codeobjects(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Conversion',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api7 CO: ", response.status_code)


def test_get_connectionList_validation(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api1 Val: ", response.status_code)


def test_get_operationList_validation(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/project/GetOperationList?projectId=1167&OperationType=Assessment',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api2 Val: ", response.status_code)


def test_get_runNumber_validation(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRunNumbers?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api3 Val: ", response.status_code)


def test_post_individualLogs_validation(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    data = {
        "projectId": "1167",
        "operationType": "Validation",
        "operationName": "null",
        "action": "null",
        "row_id": "null",
        "runno": "null"
    }
    response = requests.post(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetIndividualLogs',
        headers=headers,data=json.dumps(data))
    # print(response)
    assert response.status_code == 200
    print(" code migration api4 Val: ", response.status_code)





def test_get_requestTabledata_validation(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetRequestTableData?projectId=1167&operationType=Validation',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api5 Val: ", response.status_code)


def test_get_reportvalidation_validation(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetCommonFilesFromDirectory?path=PRJ1167SRC/undefined/Reports/Validation_Reports/',
        headers=headers)
    # print(response)
    assert response.status_code == 204
    print(" code migration api6 Val: ", response.status_code)




def test_get_projectmenu_deploy(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetSecUserProjectMenu?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api1 Dep: ", response.status_code)

def test_get_filesfromdirectory_deploy(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetFilesFromDirectory?path=PRJ1167SRC//Deployment_Logs/s',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api2 Dep: ", response.status_code)

def test_get_singlefilesdirs_deploy(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetSingleFileDirs?path=PRJ1167SRC/Single_File_Output/',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api3 Dep: ", response.status_code)


def test_get_deployoperations_deploy(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetDeployOperations',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api4 Dep: ", response.status_code)


def test_get_connectionList_deploy(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/GetConnectionList?projectId=1167',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api4 Dep: ", response.status_code)

def test_get_connectionList_deploy(token):
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json'
    }
    response = requests.get(
        'http://adobev2.qmigrator.ai/api/v1/Project/RuninfoSelect',
        headers=headers)
    # print(response)
    assert response.status_code == 200
    print(" code migration api4 Dep: ", response.status_code)
























token = getAuthToken()
test_get_connectionList(token)
test_get_objectType_storageobject(token)
test_get_runNumbers_storageobject(token)
test_post_individualLogs_storageobject(token)
test_get_requestTbaledata_storageobject(token)
test_get_reportValidation_storageobject(token)
test_get_connectionList_codeobjects(token)
test_get_objectTypes_codeobjects(token)
test_get_runNumbers_codeobjects(token)
test_post_individualLogs_codeobjects(token)
test_get_requestTabledata_codeobjects(token)
test_get_reportvalidation_codeobjects(token)
test_get_requestTabledata1_codeobjects(token)
test_get_connectionList_validation(token)
test_get_operationList_validation(token)
test_get_runNumber_validation(token)
test_post_individualLogs_validation(token)
test_get_requestTabledata_validation(token)
test_get_reportvalidation_validation(token)