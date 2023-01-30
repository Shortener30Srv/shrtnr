FROM nginx:1.21-alpine
#
RUN rm -f /etc/nginx/conf.d/default.conf
RUN rm -f /etc/nginx/conf.d/nginx_server_route.conf
COPY nginx_http.conf /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/conf.d
