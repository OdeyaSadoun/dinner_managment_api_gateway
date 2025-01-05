class HttpConstStrings:
    # ? HTTP Methods
    get_method="GET"
    post_method="POST"
    put_method="PUT"
    delete_method="DELETE"
    patch_method="PATCH"

    all_sources="*"

    # ? Prefixes
    auth_prefix="/auth"
    person_prefix="/person"
    table_prefix="/table"

    # ? Routes
    login_route = "/login"
    register_route = "/register"

    get_all_people_route = ""
    get_person_by_id_route = "/{person_id}"
    create_person_route = ""
    update_person_route = "/{person_id}"
    seat_person_route = "/seat/{person_id}"
    delete_person_route = "/delete/{person_id}"

    get_all_tables_route = ""
    get_table_by_id_route = "/{table_id}"
    create_table_route = ""
    delete_table_route = "/delete/{table_id}"
    add_person_to_table_route = "/add_person/{table_id}"
    remove_person_from_table_route = "/remove_person/{table_id}"
    update_table_position_route = "/position/{table_id}"
    update_table_route = "/{table_id}"
