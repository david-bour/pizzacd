az aks create --resource-group top-secret \
              --name pizzaAKS \
              --node-count 2 \
              --generate-ssh-keys \
              --attach-acr pizza