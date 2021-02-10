az webapp create --resource-group top-secret \
                 --plan pizza-plan \
                 --name pizza-appserver \
                 --deployment-container-image-name pizza.azurecr.io/appserver:latest

az webapp create --resource-group top-secret \
                 --plan pizza-plan \
                 --name pizza-webserver \
                 --deployment-container-image-name pizza.azurecr.io/webserver:latest