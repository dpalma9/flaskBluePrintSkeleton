# HOW TO

Build the docker image and run it:

```bash
docker build -t daniweb -f Dockerfile .
docker run -d --rm -p 8000:5000 --name testserver daniweb
```

