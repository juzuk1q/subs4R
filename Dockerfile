# ==========================================
# Stage 1: Build React Frontend
# ==========================================
FROM node:22-alpine AS frontend-builder
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY index.html vite.config.ts tsconfig*.json .oxlintrc.json ./
COPY public/ public/
COPY src/ src/
RUN npm run build

# ==========================================
# Stage 2: Build Go Backend
# ==========================================
FROM golang:1.24-alpine AS backend-builder
WORKDIR /app/backend

COPY backend/go.mod ./
RUN go mod download

COPY backend/*.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -trimpath -ldflags="-s -w" -o /app/subs4r-server .

# ==========================================
# Stage 3: Minimal Production Image
# ==========================================
FROM alpine:3.21 AS runner
WORKDIR /app

RUN apk --no-cache add ca-certificates tzdata

COPY --from=backend-builder /app/subs4r-server /app/subs4r-server
COPY --from=frontend-builder /app/dist /app/dist

EXPOSE 8080
ENV PORT=8080

CMD ["/app/subs4r-server"]
