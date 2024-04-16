def print_level_header(level_id: int, level_letters: str) -> None:
    title = f"LEVEL {level_id} ({level_letters})"
    print(title)
    print(f"{'':=>{len(title)}}")


def print_level_stage_info(stage_info: dict) -> None:
    print("\nSTAGE_INFO\n----------\n")
    print(f"{'Id':.<20}: {stage_info['stage_id']}")
    print(f"{'Country':.<20}: {stage_info['stage_country']}")
    print(f"{'Landmark':.<20}: {stage_info['stage_landmark']}")


def print_level_answers(answers: [str]) -> None:
    print("\nLEVEL ANSWERS\n-------------\n")
    for answer in answers:
        print(f"{' ':>4} * {answer}")
