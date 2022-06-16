
## Simple UI application using Python frameworks.


Run in container using Server:

```
docker run -v ${PWD}/AppManagerUI-github:/apps/AppManagerUI -p 3030:3030 anvilworks/anvil-app-server --app AppManagerUI
```

Run as stand-along container:

```
docker run -vp 3030:3030 oleggorj/app-manager-ui:0.0.1
```

Access UI: `http://localhost:3030`



## Refs

[https://github.com/anvil-works/anvil-runtime](https://github.com/anvil-works/anvil-runtime/blob/master/doc/getting-started.md)

Anvil App Server image: https://hub.docker.com/r/anvilworks/anvil-app-server

