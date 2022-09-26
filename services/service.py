def get_subs_profile_data(msisdn: str, user_login: str, out_contract_name: str, target_date: str,
                          in_contract_sign: str, db):
    parameters = {
        'outContractName': out_contract_name,
        'userLogin': user_login,
        'targetDate': target_date,
        'msisdn': msisdn,
        'inContractSign': in_contract_sign,
    }
    print(type(db))
    # result = db.get_subs_profile(parameters)
