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
    print_prefix ="/print"

    # ? Routes
    login_route = "/login"
    register_route = "/register"
    get_all_users_route = "/get_all_users"
    get_manual_people_route = "/get_manual_people"
    get_user_by_id_route = "/get_user_by_id/{user_id}"
    get_user_by_username_and_password_route = "/get_user_by_username_and_password"
    delete_user_route = "/delete_user/{user_id}"
    update_user_route = "/update_user/{user_id}"
    print_sticker_route = "/print_sticker"

    get_all_people_route = ""
    get_person_by_id_route = "/{person_id}"
    create_person_route = ""
    update_person_route = "/{person_id}"
    seat_person_route = "/seat/{person_id}"
    unseat_person_route = "/unseat/{person_id}"
    delete_person_route = "/delete/{person_id}"

    get_all_tables_route = ""
    get_table_by_id_route = "/{table_id}"
    create_table_route = ""
    delete_table_route = "/delete/{table_id}"
    add_person_to_table_route = "/add_person/{table_id}"
    remove_person_from_table_route = "/remove_person/{table_id}"
    update_table_position_route = "/position/{table_id}"
    update_table_route = "/{table_id}"
