from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository

from app.schemas.dashboard import (
    DashboardResponse,
    DashboardProject,
    DashboardContribution,
    DashboardCommunity,
)


def get_dashboard(
    db: Session,
    member_id: str,
) -> DashboardResponse:

    project = DashboardRepository.get_project(db)

    contribution = DashboardRepository.get_contribution(
        db=db,
        member_id=member_id,
    )

    scc = DashboardRepository.get_scc(
        db=db,
        member_id=member_id,
    )

    associations = DashboardRepository.get_associations(
        db=db,
        member_id=member_id,
    )

    return DashboardResponse(
        full_name=scc["full_name"],

        project=DashboardProject(
            project_name=project["project_name"],
            target_amount=project["target_amount"],
            raised_amount=project["contributed_amount"],
        ),

        contribution=DashboardContribution(
            pledge_amount=contribution["pledge_amount"],
            contributed_amount=contribution["contributed_amount"],
        ),

        scc=DashboardCommunity(
            id=str(scc["id"]),
            name=scc["name"],
            total_contributed=scc["total_contributed"],
            member_count=scc["member_count"],
        ),

        associations=[
            DashboardCommunity(
                id=str(a["id"]),
                name=a["name"],
                total_contributed=a["total_contributed"],
                member_count=a["member_count"],
            )
            for a in associations
        ],
    )