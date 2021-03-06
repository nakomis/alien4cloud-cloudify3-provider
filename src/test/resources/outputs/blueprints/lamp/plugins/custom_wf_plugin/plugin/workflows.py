from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import tasks as workflow_tasks
from utils import set_state_task
from utils import operation_task
from utils import link_tasks
from utils import CustomContext


@workflow
def a4c_uninstall(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_uninstall(ctx, graph, custom_context)
    return graph.execute()


@workflow
def a4c_install(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_install(ctx, graph, custom_context)
    return graph.execute()


def _a4c_uninstall(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    set_state_task(ctx, graph, 'Wordpress', 'deleted', 'Wordpress_deleted', custom_context)
    set_state_task(ctx, graph, 'Apache', 'stopped', 'Apache_stopped', custom_context)
    set_state_task(ctx, graph, 'Apache', 'stopping', 'Apache_stopping', custom_context)
    operation_task(ctx, graph, 'DataBase', 'cloudify.interfaces.lifecycle.delete', 'delete_DataBase', custom_context)
    set_state_task(ctx, graph, 'PHP', 'stopping', 'PHP_stopping', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.stop', 'stop_Server', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'deleting', 'DataBase_deleting', custom_context)
    set_state_task(ctx, graph, 'Server', 'deleting', 'Server_deleting', custom_context)
    set_state_task(ctx, graph, 'PHP', 'deleted', 'PHP_deleted', custom_context)
    operation_task(ctx, graph, 'InternalNetwork', 'cloudify.interfaces.lifecycle.stop', 'stop_InternalNetwork', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'stopped', 'Wordpress_stopped', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'deleted', 'InternalNetwork_deleted', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'stopping', 'Mysql_stopping', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'deleting', 'Wordpress_deleting', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'stopping', 'NetPub_stopping', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.delete', 'delete_Server', custom_context)
    operation_task(ctx, graph, 'NetPub', 'cloudify.interfaces.lifecycle.stop', 'stop_NetPub', custom_context)
    set_state_task(ctx, graph, 'Apache', 'deleting', 'Apache_deleting', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'stopped', 'InternalNetwork_stopped', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'deleted', 'NetPub_deleted', custom_context)
    set_state_task(ctx, graph, 'Server', 'stopped', 'Server_stopped', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'stopping', 'Wordpress_stopping', custom_context)
    set_state_task(ctx, graph, 'PHP', 'deleting', 'PHP_deleting', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'deleting', 'Mysql_deleting', custom_context)
    set_state_task(ctx, graph, 'Server', 'stopping', 'Server_stopping', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'deleting', 'NetPub_deleting', custom_context)
    operation_task(ctx, graph, 'DataBase', 'cloudify.interfaces.lifecycle.stop', 'stop_DataBase', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'deleted', 'DataBase_deleted', custom_context)
    set_state_task(ctx, graph, 'PHP', 'stopped', 'PHP_stopped', custom_context)
    operation_task(ctx, graph, 'InternalNetwork', 'cloudify.interfaces.lifecycle.delete', 'delete_InternalNetwork', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'stopping', 'InternalNetwork_stopping', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'stopped', 'NetPub_stopped', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'deleting', 'InternalNetwork_deleting', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'stopped', 'DataBase_stopped', custom_context)
    set_state_task(ctx, graph, 'Server', 'deleted', 'Server_deleted', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'stopped', 'Mysql_stopped', custom_context)
    operation_task(ctx, graph, 'NetPub', 'cloudify.interfaces.lifecycle.delete', 'delete_NetPub', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'stopping', 'DataBase_stopping', custom_context)
    set_state_task(ctx, graph, 'Apache', 'deleted', 'Apache_deleted', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'deleted', 'Mysql_deleted', custom_context)
    link_tasks(graph, 'Wordpress_deleted', 'Wordpress_deleting', custom_context)
    link_tasks(graph, 'Apache_stopped', 'Apache_stopping', custom_context)
    link_tasks(graph, 'Apache_stopping', 'Wordpress_deleted', custom_context)
    link_tasks(graph, 'delete_DataBase', 'DataBase_deleting', custom_context)
    link_tasks(graph, 'stop_Server', 'Server_stopping', custom_context)
    link_tasks(graph, 'DataBase_deleting', 'DataBase_stopped', custom_context)
    link_tasks(graph, 'Server_deleting', 'Server_stopped', custom_context)
    link_tasks(graph, 'PHP_deleted', 'PHP_deleting', custom_context)
    link_tasks(graph, 'stop_InternalNetwork', 'InternalNetwork_stopping', custom_context)
    link_tasks(graph, 'Wordpress_stopped', 'Wordpress_stopping', custom_context)
    link_tasks(graph, 'InternalNetwork_deleted', 'delete_InternalNetwork', custom_context)
    link_tasks(graph, 'Wordpress_deleting', 'Wordpress_stopped', custom_context)
    link_tasks(graph, 'delete_Server', 'Server_deleting', custom_context)
    link_tasks(graph, 'stop_NetPub', 'NetPub_stopping', custom_context)
    link_tasks(graph, 'Apache_deleting', 'Apache_stopped', custom_context)
    link_tasks(graph, 'InternalNetwork_stopped', 'stop_InternalNetwork', custom_context)
    link_tasks(graph, 'NetPub_deleted', 'delete_NetPub', custom_context)
    link_tasks(graph, 'Server_stopped', 'stop_Server', custom_context)
    link_tasks(graph, 'PHP_deleting', 'PHP_stopped', custom_context)
    link_tasks(graph, 'Mysql_deleting', 'Mysql_stopped', custom_context)
    link_tasks(graph, 'Server_stopping', 'Apache_deleted', custom_context)
    link_tasks(graph, 'Server_stopping', 'PHP_deleted', custom_context)
    link_tasks(graph, 'NetPub_deleting', 'NetPub_stopped', custom_context)
    link_tasks(graph, 'stop_DataBase', 'DataBase_stopping', custom_context)
    link_tasks(graph, 'DataBase_deleted', 'delete_DataBase', custom_context)
    link_tasks(graph, 'PHP_stopped', 'PHP_stopping', custom_context)
    link_tasks(graph, 'delete_InternalNetwork', 'InternalNetwork_deleting', custom_context)
    link_tasks(graph, 'NetPub_stopped', 'stop_NetPub', custom_context)
    link_tasks(graph, 'InternalNetwork_deleting', 'InternalNetwork_stopped', custom_context)
    link_tasks(graph, 'DataBase_stopped', 'stop_DataBase', custom_context)
    link_tasks(graph, 'Server_deleted', 'delete_Server', custom_context)
    link_tasks(graph, 'Mysql_stopped', 'Mysql_stopping', custom_context)
    link_tasks(graph, 'delete_NetPub', 'NetPub_deleting', custom_context)
    link_tasks(graph, 'DataBase_stopping', 'Mysql_deleted', custom_context)
    link_tasks(graph, 'Apache_deleted', 'Apache_deleting', custom_context)
    link_tasks(graph, 'Mysql_deleted', 'Mysql_deleting', custom_context)


def _a4c_install(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    set_state_task(ctx, graph, 'Apache', 'created', 'Apache_created', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.create', 'create_Server', custom_context)
    set_state_task(ctx, graph, 'Apache', 'started', 'Apache_started', custom_context)
    set_state_task(ctx, graph, 'Apache', 'configured', 'Apache_configured', custom_context)
    operation_task(ctx, graph, 'DataBase', 'cloudify.interfaces.lifecycle.create', 'create_DataBase', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'started', 'DataBase_started', custom_context)
    operation_task(ctx, graph, 'Mysql', 'cloudify.interfaces.lifecycle.configure', 'configure_Mysql', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'initial', 'Mysql_initial', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'creating', 'Mysql_creating', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'configured', 'DataBase_configured', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'configuring', 'Mysql_configuring', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'created', 'Wordpress_created', custom_context)
    set_state_task(ctx, graph, 'Apache', 'initial', 'Apache_initial', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'starting', 'Mysql_starting', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'starting', 'NetPub_starting', custom_context)
    operation_task(ctx, graph, 'Apache', 'cloudify.interfaces.lifecycle.start', 'start_Apache', custom_context)
    operation_task(ctx, graph, 'Wordpress', 'cloudify.interfaces.lifecycle.start', 'start_Wordpress', custom_context)
    operation_task(ctx, graph, 'Mysql', 'cloudify.interfaces.lifecycle.create', 'create_Mysql', custom_context)
    operation_task(ctx, graph, 'NetPub', 'cloudify.interfaces.lifecycle.create', 'create_NetPub', custom_context)
    operation_task(ctx, graph, 'PHP', 'cloudify.interfaces.lifecycle.configure', 'configure_PHP', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'starting', 'Wordpress_starting', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'creating', 'NetPub_creating', custom_context)
    set_state_task(ctx, graph, 'Apache', 'configuring', 'Apache_configuring', custom_context)
    set_state_task(ctx, graph, 'Server', 'creating', 'Server_creating', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'creating', 'Wordpress_creating', custom_context)
    operation_task(ctx, graph, 'Wordpress', 'cloudify.interfaces.lifecycle.configure', 'configure_Wordpress', custom_context)
    operation_task(ctx, graph, 'NetPub', 'cloudify.interfaces.lifecycle.configure', 'configure_NetPub', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'started', 'Mysql_started', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'initial', 'InternalNetwork_initial', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'configuring', 'InternalNetwork_configuring', custom_context)
    set_state_task(ctx, graph, 'Server', 'started', 'Server_started', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'started', 'InternalNetwork_started', custom_context)
    set_state_task(ctx, graph, 'Server', 'configuring', 'Server_configuring', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'started', 'Wordpress_started', custom_context)
    set_state_task(ctx, graph, 'Apache', 'starting', 'Apache_starting', custom_context)
    set_state_task(ctx, graph, 'PHP', 'configuring', 'PHP_configuring', custom_context)
    set_state_task(ctx, graph, 'PHP', 'configured', 'PHP_configured', custom_context)
    set_state_task(ctx, graph, 'Server', 'initial', 'Server_initial', custom_context)
    set_state_task(ctx, graph, 'Server', 'starting', 'Server_starting', custom_context)
    operation_task(ctx, graph, 'NetPub', 'cloudify.interfaces.lifecycle.start', 'start_NetPub', custom_context)
    operation_task(ctx, graph, 'InternalNetwork', 'cloudify.interfaces.lifecycle.configure', 'configure_InternalNetwork', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'creating', 'DataBase_creating', custom_context)
    operation_task(ctx, graph, 'DataBase', 'cloudify.interfaces.lifecycle.start', 'start_DataBase', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'created', 'DataBase_created', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'created', 'NetPub_created', custom_context)
    operation_task(ctx, graph, 'PHP', 'cloudify.interfaces.lifecycle.create', 'create_PHP', custom_context)
    set_state_task(ctx, graph, 'Apache', 'creating', 'Apache_creating', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'initial', 'Wordpress_initial', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'configuring', 'Wordpress_configuring', custom_context)
    set_state_task(ctx, graph, 'Wordpress', 'configured', 'Wordpress_configured', custom_context)
    set_state_task(ctx, graph, 'Server', 'configured', 'Server_configured', custom_context)
    operation_task(ctx, graph, 'DataBase', 'cloudify.interfaces.lifecycle.configure', 'configure_DataBase', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'starting', 'DataBase_starting', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'configuring', 'DataBase_configuring', custom_context)
    operation_task(ctx, graph, 'InternalNetwork', 'cloudify.interfaces.lifecycle.start', 'start_InternalNetwork', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'configured', 'Mysql_configured', custom_context)
    set_state_task(ctx, graph, 'PHP', 'created', 'PHP_created', custom_context)
    operation_task(ctx, graph, 'PHP', 'cloudify.interfaces.lifecycle.start', 'start_PHP', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'configured', 'InternalNetwork_configured', custom_context)
    operation_task(ctx, graph, 'Apache', 'cloudify.interfaces.lifecycle.configure', 'configure_Apache', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'created', 'InternalNetwork_created', custom_context)
    set_state_task(ctx, graph, 'PHP', 'started', 'PHP_started', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'starting', 'InternalNetwork_starting', custom_context)
    set_state_task(ctx, graph, 'DataBase', 'initial', 'DataBase_initial', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'initial', 'NetPub_initial', custom_context)
    set_state_task(ctx, graph, 'InternalNetwork', 'creating', 'InternalNetwork_creating', custom_context)
    set_state_task(ctx, graph, 'PHP', 'starting', 'PHP_starting', custom_context)
    set_state_task(ctx, graph, 'PHP', 'initial', 'PHP_initial', custom_context)
    set_state_task(ctx, graph, 'PHP', 'creating', 'PHP_creating', custom_context)
    set_state_task(ctx, graph, 'Mysql', 'created', 'Mysql_created', custom_context)
    operation_task(ctx, graph, 'Apache', 'cloudify.interfaces.lifecycle.create', 'create_Apache', custom_context)
    operation_task(ctx, graph, 'InternalNetwork', 'cloudify.interfaces.lifecycle.create', 'create_InternalNetwork', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'configured', 'NetPub_configured', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'configuring', 'NetPub_configuring', custom_context)
    operation_task(ctx, graph, 'Mysql', 'cloudify.interfaces.lifecycle.start', 'start_Mysql', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.configure', 'configure_Server', custom_context)
    set_state_task(ctx, graph, 'NetPub', 'started', 'NetPub_started', custom_context)
    operation_task(ctx, graph, 'Wordpress', 'cloudify.interfaces.lifecycle.create', 'create_Wordpress', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.start', 'start_Server', custom_context)
    set_state_task(ctx, graph, 'Server', 'created', 'Server_created', custom_context)
    link_tasks(graph, 'Apache_created', 'create_Apache', custom_context)
    link_tasks(graph, 'create_Server', 'Server_creating', custom_context)
    link_tasks(graph, 'Apache_started', 'start_Apache', custom_context)
    link_tasks(graph, 'Apache_configured', 'configure_Apache', custom_context)
    link_tasks(graph, 'create_DataBase', 'DataBase_creating', custom_context)
    link_tasks(graph, 'DataBase_started', 'start_DataBase', custom_context)
    link_tasks(graph, 'configure_Mysql', 'Mysql_configuring', custom_context)
    link_tasks(graph, 'Mysql_initial', 'DataBase_started', custom_context)
    link_tasks(graph, 'Mysql_creating', 'Mysql_initial', custom_context)
    link_tasks(graph, 'DataBase_configured', 'configure_DataBase', custom_context)
    link_tasks(graph, 'Mysql_configuring', 'Wordpress_created', custom_context)
    link_tasks(graph, 'Mysql_configuring', 'Mysql_created', custom_context)
    link_tasks(graph, 'Wordpress_created', 'create_Wordpress', custom_context)
    link_tasks(graph, 'Apache_initial', 'Server_started', custom_context)
    link_tasks(graph, 'Mysql_starting', 'Mysql_configured', custom_context)
    link_tasks(graph, 'NetPub_starting', 'NetPub_configured', custom_context)
    link_tasks(graph, 'start_Apache', 'Apache_starting', custom_context)
    link_tasks(graph, 'start_Wordpress', 'Wordpress_starting', custom_context)
    link_tasks(graph, 'create_Mysql', 'Mysql_creating', custom_context)
    link_tasks(graph, 'create_NetPub', 'NetPub_creating', custom_context)
    link_tasks(graph, 'configure_PHP', 'PHP_configuring', custom_context)
    link_tasks(graph, 'Wordpress_starting', 'Wordpress_configured', custom_context)
    link_tasks(graph, 'NetPub_creating', 'NetPub_initial', custom_context)
    link_tasks(graph, 'Apache_configuring', 'Apache_created', custom_context)
    link_tasks(graph, 'Server_creating', 'Server_initial', custom_context)
    link_tasks(graph, 'Wordpress_creating', 'Wordpress_initial', custom_context)
    link_tasks(graph, 'configure_Wordpress', 'Wordpress_configuring', custom_context)
    link_tasks(graph, 'configure_NetPub', 'NetPub_configuring', custom_context)
    link_tasks(graph, 'Mysql_started', 'start_Mysql', custom_context)
    link_tasks(graph, 'InternalNetwork_configuring', 'DataBase_created', custom_context)
    link_tasks(graph, 'InternalNetwork_configuring', 'InternalNetwork_created', custom_context)
    link_tasks(graph, 'InternalNetwork_configuring', 'Server_created', custom_context)
    link_tasks(graph, 'Server_started', 'start_Server', custom_context)
    link_tasks(graph, 'InternalNetwork_started', 'start_InternalNetwork', custom_context)
    link_tasks(graph, 'Server_configuring', 'InternalNetwork_started', custom_context)
    link_tasks(graph, 'Server_configuring', 'NetPub_started', custom_context)
    link_tasks(graph, 'Server_configuring', 'Server_created', custom_context)
    link_tasks(graph, 'Wordpress_started', 'start_Wordpress', custom_context)
    link_tasks(graph, 'Apache_starting', 'Apache_configured', custom_context)
    link_tasks(graph, 'PHP_configuring', 'PHP_created', custom_context)
    link_tasks(graph, 'PHP_configuring', 'Wordpress_created', custom_context)
    link_tasks(graph, 'PHP_configured', 'configure_PHP', custom_context)
    link_tasks(graph, 'Server_starting', 'Server_configured', custom_context)
    link_tasks(graph, 'start_NetPub', 'NetPub_starting', custom_context)
    link_tasks(graph, 'configure_InternalNetwork', 'InternalNetwork_configuring', custom_context)
    link_tasks(graph, 'DataBase_creating', 'DataBase_initial', custom_context)
    link_tasks(graph, 'start_DataBase', 'DataBase_starting', custom_context)
    link_tasks(graph, 'DataBase_created', 'create_DataBase', custom_context)
    link_tasks(graph, 'NetPub_created', 'create_NetPub', custom_context)
    link_tasks(graph, 'create_PHP', 'PHP_creating', custom_context)
    link_tasks(graph, 'Apache_creating', 'Apache_initial', custom_context)
    link_tasks(graph, 'Wordpress_initial', 'Apache_started', custom_context)
    link_tasks(graph, 'Wordpress_configuring', 'Mysql_started', custom_context)
    link_tasks(graph, 'Wordpress_configuring', 'Wordpress_created', custom_context)
    link_tasks(graph, 'Wordpress_configuring', 'PHP_started', custom_context)
    link_tasks(graph, 'Wordpress_configured', 'configure_Wordpress', custom_context)
    link_tasks(graph, 'Server_configured', 'configure_Server', custom_context)
    link_tasks(graph, 'configure_DataBase', 'DataBase_configuring', custom_context)
    link_tasks(graph, 'DataBase_starting', 'DataBase_configured', custom_context)
    link_tasks(graph, 'DataBase_configuring', 'DataBase_created', custom_context)
    link_tasks(graph, 'DataBase_configuring', 'InternalNetwork_started', custom_context)
    link_tasks(graph, 'start_InternalNetwork', 'InternalNetwork_starting', custom_context)
    link_tasks(graph, 'Mysql_configured', 'configure_Mysql', custom_context)
    link_tasks(graph, 'PHP_created', 'create_PHP', custom_context)
    link_tasks(graph, 'start_PHP', 'PHP_starting', custom_context)
    link_tasks(graph, 'InternalNetwork_configured', 'configure_InternalNetwork', custom_context)
    link_tasks(graph, 'configure_Apache', 'Apache_configuring', custom_context)
    link_tasks(graph, 'InternalNetwork_created', 'create_InternalNetwork', custom_context)
    link_tasks(graph, 'PHP_started', 'start_PHP', custom_context)
    link_tasks(graph, 'InternalNetwork_starting', 'InternalNetwork_configured', custom_context)
    link_tasks(graph, 'InternalNetwork_creating', 'InternalNetwork_initial', custom_context)
    link_tasks(graph, 'PHP_starting', 'PHP_configured', custom_context)
    link_tasks(graph, 'PHP_initial', 'Server_started', custom_context)
    link_tasks(graph, 'PHP_creating', 'PHP_initial', custom_context)
    link_tasks(graph, 'Mysql_created', 'create_Mysql', custom_context)
    link_tasks(graph, 'create_Apache', 'Apache_creating', custom_context)
    link_tasks(graph, 'create_InternalNetwork', 'InternalNetwork_creating', custom_context)
    link_tasks(graph, 'NetPub_configured', 'configure_NetPub', custom_context)
    link_tasks(graph, 'NetPub_configuring', 'NetPub_created', custom_context)
    link_tasks(graph, 'NetPub_configuring', 'Server_created', custom_context)
    link_tasks(graph, 'start_Mysql', 'Mysql_starting', custom_context)
    link_tasks(graph, 'configure_Server', 'Server_configuring', custom_context)
    link_tasks(graph, 'NetPub_started', 'start_NetPub', custom_context)
    link_tasks(graph, 'create_Wordpress', 'Wordpress_creating', custom_context)
    link_tasks(graph, 'start_Server', 'Server_starting', custom_context)
    link_tasks(graph, 'Server_created', 'create_Server', custom_context)


#following code can be pasted in src/test/python/workflows/context.py for simulation
#def _build_nodes(ctx):
    #types = []
    #types.append('alien.nodes.openstack.PrivateNetwork')
    #types.append('alien.nodes.PrivateNetwork')
    #types.append('tosca.nodes.Network')
    #types.append('tosca.nodes.Root')
    #node_InternalNetwork = _build_node(ctx, 'InternalNetwork', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_Server = _build_node(ctx, 'Server', types, 1)
    #types = []
    #types.append('alien.nodes.Wordpress')
    #types.append('tosca.nodes.WebApplication')
    #types.append('tosca.nodes.Root')
    #node_Wordpress = _build_node(ctx, 'Wordpress', types, 1)
    #types = []
    #types.append('alien.nodes.Mysql')
    #types.append('tosca.nodes.Database')
    #types.append('tosca.nodes.Root')
    #node_Mysql = _build_node(ctx, 'Mysql', types, 1)
    #types = []
    #types.append('alien.nodes.PHP')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_PHP = _build_node(ctx, 'PHP', types, 1)
    #types = []
    #types.append('alien.nodes.Apache')
    #types.append('tosca.nodes.WebServer')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_Apache = _build_node(ctx, 'Apache', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.PublicNetwork')
    #types.append('alien.nodes.PublicNetwork')
    #types.append('tosca.nodes.Network')
    #types.append('tosca.nodes.Root')
    #node_NetPub = _build_node(ctx, 'NetPub', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_DataBase = _build_node(ctx, 'DataBase', types, 1)
    #_add_relationship(node_Server, node_InternalNetwork)
    #_add_relationship(node_Server, node_NetPub)
    #_add_relationship(node_Wordpress, node_Apache)
    #_add_relationship(node_Wordpress, node_Mysql)
    #_add_relationship(node_Wordpress, node_PHP)
    #_add_relationship(node_Mysql, node_DataBase)
    #_add_relationship(node_PHP, node_Server)
    #_add_relationship(node_Apache, node_Server)
    #_add_relationship(node_DataBase, node_InternalNetwork)
