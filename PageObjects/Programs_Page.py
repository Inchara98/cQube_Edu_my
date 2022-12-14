class Program_Objects:
    # List of Selenium attributes of Program Screen
    L = r'L\.|[^\d.]'
    dashboard = "menu-item-0"
    Diksha = "menu-item-2"
    nishtha = "menu-item-1"
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"

    # Tab xpath locators
    Implementation_Status_tab = "//*[contains(text(),'Implementation Status')]"
    Course_medium_tab = "//*[contains(text(),'Courses and Mediums status')]"
    Potential_Base_tab = "//*[contains(text(),'% against Potential Base')]"
    District_wise_tab = "//*[contains(text(),'District wise Status')]"
    Course_wise_tab = "//*[contains(text(),'Course wise Status ')]"

    total_state = "//app-nishtha/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    total_enrollment = "//app-nishtha/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    total_completion = "//app-nishtha/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    total_certification = "//app-nishtha/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    total_medium = "//app-nishtha/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    total_state_Tittle = "//app-nishtha/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    total_enrollment_Tittle = "//app-nishtha/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    total_completion_Tittle = "//app-nishtha/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    total_certification_Tittle = "//app-nishtha/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    total_medium_Tittle = "//app-nishtha/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"
    Select_Program_Dropdown = ""
    Clear_Button = "//*[@id='filter-Program']/div/span[1]"
    program_logfile = "../../../Logs/Program.log"
    Program_dropdown = "ng-option-label ng-star-inserted"

    # Implementation Status
    Implementation_Status = "mat-tab-label-1-0"
    FullScreen = ""
    Zoomin = ""
    Zoomout = ""

    # Courses and Medium status
    state_colmn = "//*[@role='row']/td[1]"
    course_launch = "//*[@role='row']/td[2]"
    Medium = "//*[@role='row']/td[3]"
    CM_status = "mat-tab-label-0-1"
    dropdown_options = "//div[@role='option']/span"
    Choose_Program = "//div[@role='combobox']/input"
    choose_states = "//*[@id='filter-State/UT']/div/div/div[3]/input"
    Nishtha_1 = "//div[@role='option']/span[contains(text(),'NISHTHA 1.0')]"
    Nishtha_2 = "//div[@role='option']/span[contains(text(),'NISHTHA 2.0')]"
    Nishtha_3 = "//div[@role='option']/span[contains(text(),'NISHTHA 3.0')]"

    state_header = "//div[contains(text(),'State/UT Name')]"
    course_header = "//div[contains(text(),'Total Courses Launched')]"
    medium_header = "//div[contains(text(),'Total Mediums')]"

    state_sort = "//th[@role='columnheader'][1]"
    course_sort = "//th[@role='columnheader'][2]"
    medium_sort = "//th[@role='columnheader'][3]"

    state_values = "//td[1]"
    course_values = "//td[2]"
    medium_values = "//td[3]"

    # % against potential base
    Potential_Base = "mat-tab-label-2-3"

    # District Wise Status
    District_Status = "mat-tab-label-2-3"
    click_district_program = "//ng-select[@id='filter-Program']/div/div/div[3]/input"
    click_state_options = "//ng-select[@id='filter-State/UT']/div/div/div[3]/input"
    state_names_id = "aff430dd515c-"

    # Course wise Tab
    Course_Status = "mat-tab-label-0-4"

    Course_Status = "mat-tab-label-0-4"

    # Micro_improvements program
    dashboard = "menu-item-0"
    Micro_improvements = "menu-item-3"
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    total_Micro_improvements_ongoing_value = "//app-improvement-program/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    total_Micro_improvements_ongoing_text = "//app-improvement-program/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    total_Micro_improvements_ongoing_info = "//app-improvement-program/div[1]/div/div[1]/sb-cqube-info-card/div/img"
    total_micro_improvements_started_info = "//app-improvement-program/div[1]/div/div[2]/sb-cqube-info-card/div/img"
    total_micro_improvements_started_number = "//app-improvement-program/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_started_text = "//app-improvement-program/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    total_micro_improvements_in_progress_info = "//app-improvement-program/div[1]/div/div[3]/sb-cqube-info-card/div/img"
    total_micro_improvements_in_progress_value = "//app-improvement-program/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_in_progress_text = "//app-improvement-program/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    total_micro_improvements_in_submitted_info = "//app-improvement-program/div[1]/div/div[4]/sb-cqube-info-card/div/img"
    total_micro_improvements_in_submitted_value = "//app-improvement-program/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_in_submitted_text = "//app-improvement-program/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    total_micro_improvements_in_submitted_with_evidence_info = "//app-improvement-program/div[1]/div/div[5]/sb-cqube-info-card/div/img"
    total_micro_improvements_in_submitted_with_evidence_value = "//app-improvement-program/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_in_submitted_with_evidence_text = "//app-improvement-program/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"

    # Implementation Status micro-improvements
    Implementation_Status_micro_improvements = "//app-improvement-program/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[1]"

    # improvements status micro improvements
    improvements_status_micro_improvements = '//*[text()="Improvements Status"]'
    dropdown_option = '//app-improvement-program/div[2]/mat-tab-group/div/mat-tab-body[2]/div/div/div/div/div[' \
                      '2]/div/div/app-level-n-metric-filter-panel/div/div/ng-select '
    Choose_metrics = '//*[@id="metricFilter-Metrics to be shown"]/div/div/div[1]'
    Total_micro_improvements = '//*[@id="af316e86d9fa-0"]/span'
    micro_improvements_started = '//*[@id="af316e86d9fa-1"]'
    micro_improvements_in_progress = '//*[@id="af316e86d9fa-2"]/span'
    micro_improvements_submitted = '//*[@id="af316e86d9fa-3"]/span'
    micro_improvements_submitted_with_evidence = '//*[@id="af316e86d9fa-4"]/span'

    # Diksha Program
    Totalstates_info = "//app-digital-learning/div[1]/div/div[1]/sb-cqube-info-card/div/img"
    Totalstates_UT = "//app-digital-learning/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    Totalstates_text = "//app-digital-learning/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    Total_ETB_info = "//app-digital-learning/div[1]/div/div[2]/sb-cqube-info-card/div/img"
    Total_ETB = "//app-digital-learning/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    Total_ETB_text = "//app-digital-learning/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    Total_QR_Code_info = "//app-digital-learning/div[1]/div/div[3]/sb-cqube-info-card/div/img"
    Total_QR_Code = "//app-digital-learning/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    Total_QR_Code_text = "//app-digital-learning/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    Total_Content_info = "//app-digital-learning/div[1]/div/div[4]/sb-cqube-info-card/div/img"
    Total_Content = "//app-digital-learning/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    Total_Content_text = "//app-digital-learning/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    Total_time_spent_info = "//app-digital-learning/div[1]/div/div[5]/sb-cqube-info-card/div/img"
    Total_time_spent = "//app-digital-learning/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    Total_time_spent_text = "//app-digital-learning/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"

    ETB_Coverage_Tab = "//*[contains(text(),'ETB Coverage Status')]//ancestor::div[1]"
    State_column = "//th[@role='columnheader'][1]"
    Curiculum_Textbook_column = "//th[@role='columnheader'][2]"
    Energised_Textbook_column = "//th[@role='columnheader'][3]"
    per_Energised_Textbook_column = "//th[@role='columnheader'][4]"
    State_header = "//div[contains(text(),'State/UT name')]"
    Curiculum_Textbook_header = "//div[contains(text(),'Total Curriculum Textbooks')]"
    Energised_Textbook_header = "//div[contains(text(),'Total Energized Textbooks')]"
    per_Energised_Textbook_header = "//div[contains(text(),'% Energized Textbooks')]"

    Content_Coverage_Tab = "//*[contains(text(),'Content Coverage on QR')]//ancestor::div[1]"

    Learning_session_potential_tab = "//*[contains(text(),'Learning Sessions on Potential Users')]//ancestor::div[1]"

    Learning_session_tab = "//*[contains(text(),'Learning Sessions')]//ancestor::div[1]"

    # PM Poshina
    pm_poshan = "menu-item-4"
    pm_states_info = "//app-nutrition-health/div[1]/div/div[1]/sb-cqube-info-card/div/img"
    pm_state_value = "//app-nutrition-health/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    pm_state_title = "//app-nutrition-health/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"

    pm_schools_info = "//app-nutrition-health/div[1]/div/div[2]/sb-cqube-info-card/div/img"
    pm_schools_value = "//app-nutrition-health/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    pm_schools_title = "//app-nutrition-health/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"

    pm_implementation_tab = "//*[contains(text(),'Implementation Status')]"
    pm_progress_status_tab = "//*[contains(text(),'Progress Status')]"

    pm_state_btn = "button-0"
    pm_District_btn = "button-1"
    metric_options = "//*[@role='option']"
    choose_metrics = "//*[@class='ng-input']/input"

    # PGI
    pgi_button = "menu-item-7"
    learning_info = "//app-school-education/div[1]/div/div[1]/sb-cqube-info-card/div/img"
    learning_value = "//app-school-education/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    learning_text = "//app-school-education/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"

    access_info = "//app-school-education/div[1]/div/div[2]/sb-cqube-info-card/div/img"
    access_value = "//app-school-education/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    access_text = "//app-school-education/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"

    infrastructure_info = "//app-school-education/div[1]/div/div[3]/sb-cqube-info-card/div/img"
    infrastructure_value = "//app-school-education/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    infrastructure_text = "//app-school-education/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"

    equity_info = "//app-school-education/div[1]/div/div[4]/sb-cqube-info-card/div/img"
    equity_value = "//app-school-education/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    equity_text = "//app-school-education/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"

    governance_info = "//app-school-education/div[1]/div/div[5]/sb-cqube-info-card/div/img"
    governance_value = "//app-school-education/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    governance_text = "//app-school-education/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"

    implementation_tab_result = "//*[@role='tab'][1]"
    statewise_perf_tab_result = "//*[@role='tab'][2]"
    districtwise_tab_result = "//*[@role='tab'][3]"

    pgi_state_wise_tab = "//*[contains(text(),'State Wise Performance')]"
    pgi_district_wise_tab = "//*[contains(text(),'District Wise Performance')]"

    metrics_click = "ng-input"