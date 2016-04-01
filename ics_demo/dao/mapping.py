from ics_demo.dao import rabbit_dao, carrot_dao, corps_dao
from ics_demo.dao import mon_dao, osd_dao, vsan_dao, host_dao, block_dao

demo_dao_mapping = {'rabbit': rabbit_dao,
                    'carrot': carrot_dao,
                    'corps': corps_dao,
                    'mon': mon_dao,
                    'osd': osd_dao,
                    'vsan': vsan_dao,
                    'block': block_dao,
                    'host': host_dao,
                    }
dao_mapping = dict(demo_dao_mapping.items())
