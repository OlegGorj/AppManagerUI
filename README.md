
## Simple UA application using Python frameworks.


Run in container using Server:

```
docker run -v ${PWD}/AppManagerUI-github:/apps/AppManagerUI -p 3030:3030 anvilworks/anvil-app-server --app AppManagerUI
```

Run as stand-along container:

```
docker run -vp 3030:3030 oleggorj/app-manager-ui:0.0.1
```

Access UI: `http://localhost:3030`
