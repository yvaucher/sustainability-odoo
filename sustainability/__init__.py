# © 2021 Open Net Sarl
# © 2024 Camptocamp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from . import models
from . import tests


def _pre_init_sustainability(env):
    pass
    """ Allow installing sustainability in databases with large account.move.line table
        (>400k records)
        - Creating the computed+stored fields of carbon emissions on account.move.line
          is terribly slow with the ORM and leads to "Out of Memory" crashes
    """
    env.cr.execute(
        "ALTER TABLE account_move_line"
        " ADD COLUMN IF NOT EXISTS carbon_data_uncertainty_percentage double precision"
    )
    env.cr.execute(
        "ALTER TABLE account_move_line"
        " ADD COLUMN IF NOT EXISTS carbon_data_uncertainty_percentage double precision"
    )
    env.cr.execute(
        "ALTER TABLE account_move_line"
        " ADD COLUMN IF NOT EXISTS carbon_data_uncertainty_value numeric"
    )
    env.cr.execute(
        "ALTER TABLE account_move_line ADD COLUMN IF NOT EXISTS carbon_dept numeric"
    )
    env.cr.execute(
        "ALTER TABLE account_move_line ADD COLUMN IF NOT EXISTS carbon_origin_json jsonb"
    )
