from ics_demo.dao import rabbit_dao, carrot_dao, corps_dao

demo_dao_mapping = {'rabbit' : rabbit_dao, 'carrot' : carrot_dao, 'corps' : corps_dao}
dao_mapping = dict(demo_dao_mapping.items())
