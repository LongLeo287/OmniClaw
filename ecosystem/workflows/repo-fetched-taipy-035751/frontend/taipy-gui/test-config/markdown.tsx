import React, { ReactNode } from "react";

interface ChildrenProps {
    children: ReactNode;
}

const ReactMarkdownMock = ({ children }: ChildrenProps) => <p>{children}</p>;

export default ReactMarkdownMock;
