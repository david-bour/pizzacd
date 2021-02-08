az webapp create --resource-group top-secret \
                 --plan pizza-plan \
                 --name pizza-appserver \
                 --deployment-container-image-name pizza.azurecr.io/appserver:latest

