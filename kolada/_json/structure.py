def _metadata(group):
    return (
        str(group["id"]),
        str(group["prel_publication_date"]),
        str(group["municipality_type"]),
        str(group["publ_period"]),
        str(group["operating_area"]),
        str(group["auspices"]),
        str(group["publication_date"]),
        str(group["perspective"]),
        str(group["is_divided_by_gender"]),
        str(group["ou_publication_date"]),
        str(group["has_ou_data"]),
        str(group["title"]),
        str(group["description"]),
    )


def _id_title(group):
    return (str(group["id"]), str(group["title"]))


def _data(group, member, _subclass):
    if _subclass in ["Municipality", "Kpi"]:
        return (
            group["kpi"],
            group["municipality"],
            group["period"],
            member["value"],
            member["gender"],
        )
    elif _subclass == "Ou":
        return (
            group["kpi"],
            group["ou"],
            group["period"],
            member["value"],
            member["gender"],
        )
    else:
        raise Exception()  # write custom exception


def _ou_structure(group):
    return (group["id"], group["municipality"], group["title"])


COLUMNS_ID_TITLE = ["id", "title"]

COLUMNS_DATA = ["kpi", "municipality", "period", "value", "gender"]

COLUMNS_METADATA = [
    "id",
    "prel_publication_date",
    "municipality_type",
    "publ_period",
    "operating_area",
    "auspices",
    "publication_date",
    "perspective",
    "is_divided_by_gender",
    "ou_publication_date",
    "has_ou_data",
    "title",
    "description",
]
