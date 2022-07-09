
## Simple UI application using Python frameworks.


1) Run in container using Server:

```
docker run -v ${PWD}/AppManagerUI-github:/apps/AppManagerUI -p 3030:3030 anvilworks/anvil-app-server --app AppManagerUI
```

2) Run as stand-along container.

Build image:

```
docker build -t oleggorj/app-manager-ui:0.0.1 .
docker push oleggorj/app-manager-ui:0.0.1
```

Run container:

```
docker run -p 3030:3030 oleggorj/app-manager-ui:0.0.1
```

Access UI:

`http://localhost:3030`


---
