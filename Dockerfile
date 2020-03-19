FROM xucheng/texlive-full:latest

COPY \
  README.md \
  entrypoint.sh \
  /root/

ENTRYPOINT ["/root/entrypoint.sh"]