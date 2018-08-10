import dash_html_components as html
import dash_core_components as dcc

def s(string_block):
    return string_block.replace('    ', '')

layout = html.Div([
    html.H1('Dash Deployment Server Documentation'),
    dcc.Markdown(s('''

        [insert text about DDS documentation]

    ''')),
    html.H2('Contents'),
    dcc.Markdown(s('''
    ***
    ''')),
    html.H3(dcc.Link('Authenticating to Plotly Enterprise with SSH',
                     href='/dash-deployment-server/ssh')),
    html.H3(dcc.Link('Deploy Dash Apps on Plotly Enterprise',
                     href='/dash-deployment-server/deployment')),
    html.H3(dcc.Link('Dash App Authentication',
                     href='/dash-deployment-server/app-authentication')),
    html.H3(dcc.Link('Configuring System Dependencies ',
                     href='/dash-deployment-server/configure-system-dependencies')),
    html.H3(dcc.Link('Linking a Redis Database',
                     href='/dash-deployment-server/redis-database')),
    html.H3(dcc.Link('Setting Enviornment Variables',
                     href='/dash-deployment-server/enviornment-variables')),
    html.H3(dcc.Link('Mapping Local Directories',
                     href='/dash-deployment-server/map-local-directories')),
    html.H3(dcc.Link('Troubleshooting App Deployment',
                     href='/dash-deployment-server/troubleshooting')),
])
