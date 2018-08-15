import dash_html_components as html
import dash_core_components as dcc

import reusable_components

def s(string_block):
    return string_block.replace('    ', '')

layout = html.Div(className='toc', children=[
    html.H1('Dash Deployment Server Documentation'),

    reusable_components.Section("What's Dash Deployment Server?", [
        reusable_components.Chapter('Dash Deployment Server',
                'https://plot.ly/dash/pricing/',
                """Dash Deployment Server is Plotly's commercial offering
                   for hosting and sharing Dash apps on-premises or in the
                   cloud.""")
    ]),

    reusable_components.Section("Deployment", [
        reusable_components.Chapter('Authenticating to Plotly Enterprise with SSH',
                '/dash-deployment-server/ssh',
                'In order to use SSH you need to generate and add a SSH key to ' \
                'the Dash Deployment Server.'),
        reusable_components.Chapter('Initialize Dash Apps on Plotly Enterprise',
                '/dash-deployment-server/initialize',
                'Initialize an app via Dash Deployment Server UI.'),
        reusable_components.Chapter('Dash App Requirements',
                '/dash-deployment-server/deploy-requirements',
                'Ensure that your app meets all the requirements for deployment.'),
        reusable_components.Chapter('Deploy Dash Apps on Plotly Enterprise',
                '/dash-deployment-server/deployment',
                'Deploy dash apps to the Dash Deployment Server using ' \
                'HTTPS or SSH. Clone, create a new, or deploy an exisiting ' \
                'app.')
    ]),

    reusable_components.Section("Configuration", [
        reusable_components.Chapter('Configuring System Dependencies',
                '/dash-deployment-server/configure-system-dependencies',
                'Install and configure system dependencies such as database drivers or the Java JRE environment.'),
        reusable_components.Chapter('Setting Enviornment Variables',
                '/dash-deployment-server/enviornment-variables',
                'Environment variables are config values that can affect the ' \
                'way your app behaves.'),
        reusable_components.Chapter('Mapping Local Directories',
                '/dash-deployment-server/map-local-directories',
                'Directory mappings allow you to make directories on the '
                'Dash Deployment Server available to your app.')
    ]),

    reusable_components.Section("Advanced", [
        reusable_components.Chapter('Dash App Authentication',
                '/dash-deployment-server/app-authentication',
                'Using `dash-auth` package to provide login through ' \
                'Plotly Enterprise.'),
        reusable_components.Chapter('Linking a Redis Database',
                '/dash-deployment-server/redis-database',
                'Create and link an in-memory database to your dash apps.')
    ]),

    reusable_components.Section("Troubleshooting", [
        reusable_components.Chapter('App Analytics',
                '/dash-deployment-server/analytics',
                """View app analytics such as last updated, CPU usage, Memory Usage, plus more."""),
        reusable_components.Chapter('App Logs',
                '/dash-deployment-server/logs',
                """Check your dash app's logs via the Dash Deployment Server
                UI or via the command line."""),
        reusable_components.Chapter('Common Errors',
                '/dash-deployment-server/troubleshooting',
                """Common errors when deploying dash apps."""),
        reusable_components.Chapter('Support',
                '/dash-deployment-server/support',
                """Having trouble deploying your app?""")
    ])
])
