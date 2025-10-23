// types.ts
export interface User {
  id: string;
  username: string;
  email: string;
  password: string;
  role: 'admin' | 'user';
}

export interface AuthToken {
  token: string;
  expiresAt: number;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
}

export interface ErrorResponse {
  error: string;
  statusCode: number;
}

export interface AuthGatewayOptions {
  baseUrl: string;
  timeout: number;
}

export enum Role {
  Admin = 'admin',
  User = 'user',
} 

export interface JWTToken {
  sub: string;
  exp: number;
  iat: number;
  role: Role;
}