class ConstStrings:
    localhost = "0.0.0.0"
    zmq_server_host = "0.0.0.0"
    business_logic_host = "business_logic"
    base_tcp_connection_strings = "tcp://"

    # ? HTTP Methods
    get_method="GET"
    post_method="POST"
    put_method="PUT"
    delete_method="DELETE"
    patch_method="PATCH"

    all_sources="*"

    # ? Prefixes
    person_prefix="/person"
    pakash_prefix="/pakash"

    # ? Routes
    get_all_people_route = ""
    get_person_by_id_route = "/{person_id}"
    get_person_by_personal_number_route = "/get_by_personal_number"
    create_person_route = ""
    update_person_route = "/{person_id}"
    delete_person_route = "/{person_id}"
    get_pakash_by_dates_route = "/get_pakash_by_dates"
    shuffle_pakash_route = ""
    update_pakash_route = ""

    # ? Messages
    error_message="error"
    success_message="success"

    # ? Request format identifiers
    resource_identifier = "resource"
    operation_identifier = "operation"
    data_identifier = "data"
    status_identifier = "status"

    # ? Resources
    person_resource = "person"
    pakash_resource = "pakash"

    # ? Data fields
    person_id_key = "person_id"
    personal_number_key = "personal_number"
    person_key = "person"
    start_date_key = "start_date"
    end_date_key = "end_date"
    updated_pakash_key = "updated_pakash"

    # ? Operations
    get_all_people_operation = "get_all_people"
    get_person_by_id_operation = "get_person_by_id"
    get_person_by_personal_number_operation = "get_person_by_personal_number"
    create_person_operation = "create_person"
    update_person_operation = "update_person"
    delete_person_operation = "delete_person"
    get_pakash_by_dates_operation = "get_pakash_by_dates"
    shuffle_pakash_operation = "shuffle_pakash"
    update_pakash_operation = "update_pakash"

    date_format = "%Y-%m-%d"