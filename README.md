# mc-portfolio-backend

get info for the azure credentials secret

az ad sp create-for-rbac --name "githubAction" --role contributor \
                            --scopes /subscriptions/<subscription>/resourceGroups/<resourcegroup> \
                                                    --sdk-auth

