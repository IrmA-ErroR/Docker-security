# базовый образ nginx на основе alpine
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
# nginx в фоновом режиме
CMD ["nginx", "-g", "daemon off;"]