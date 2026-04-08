import React, { ReactNode } from "react";

interface ChildrenProps {
    children: ReactNode;
}

export const ErrorBoundary = ({ children }: ChildrenProps) => <>{children}</>;
