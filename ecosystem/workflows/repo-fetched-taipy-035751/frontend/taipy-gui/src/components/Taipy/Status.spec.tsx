/*
 * Copyright 2021-2025 Avaiga Private Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 * an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */

import React from "react";
import {render} from "@testing-library/react";
import "@testing-library/jest-dom";
import userEvent from "@testing-library/user-event";

import { PlusOneOutlined } from "@mui/icons-material";

import Status, { StatusType } from './Status';

const status: StatusType = {status: "status", message: "message"};

describe("Status Component", () => {
    it("renders", async () => {
        const {getByText} = render(<Status value={status} />);
        const elt = getByText("message");
        const av = getByText("S");
        expect(elt.tagName).toBe("SPAN");
        expect(av.tagName).toBe("DIV");
    })
    it("uses the class", async () => {
        const {getByText} = render(<Status value={status} className="taipy-status" />);
        const elt = getByText("message");
        expect(elt.parentElement).toHaveClass("taipy-status");
    })
    it("can be closed", async () => {
        const myClose = jest.fn();
        const {getByTestId} = render(<Status value={status} onClose={myClose} />);
        const elt = getByTestId("CancelIcon");
        await userEvent.click(elt);
        expect(myClose).toHaveBeenCalled();
    })
    it("displays the open icon", async () => {
        const {getByTestId} = render(<Status value={status} openedIcon={<PlusOneOutlined/>} onClose={jest.fn()} />);
        getByTestId("PlusOneOutlinedIcon");
    })
     // Test case for Inline SVG content
     it("renders an Avatar with inline SVG", () => {
        const inlineSvg = "<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24'><circle cx='12' cy='12' r='10' fill='red'/></svg>";
        const { getByTestId } = render(<Status value={status} icon={inlineSvg} />);
        const avatar = getByTestId("Avatar");
        // Inline SVG should be rendered as inner HTML inside the Avatar
        const svgElement = avatar.querySelector("svg");
        expect(svgElement).toBeInTheDocument();
    });

    // Test case for Text content (default behavior)
    it("renders Avatar with initial when icon is text", () => {
        const { getByTestId } = render(<Status value={status} icon="Text content" />);
        const avatar = getByTestId("Avatar");
        expect(avatar).toHaveTextContent("S");
    });

    // Test case for empty content
    it("renders Avatar with initial when no icon is provided", () => {
        const { getByTestId } = render(<Status value={status} />);
        const avatar = getByTestId("Avatar");
        expect(avatar).toHaveTextContent("S");
    });

    // Test case for an invalid content type (like a non-SVG string)
    it("renders Avatar with initial if icon is invalid", () => {
        const { getByTestId } = render(<Status value={status} icon="invalid-content" />);
        const avatar = getByTestId("Avatar");
        expect(avatar).toHaveTextContent("S");
    });

    it("renders an avatar with initial when icon is false", () => {
        const statusWithoutIcons: StatusType = { status: "warning", message: "Warning detected" };

        const { getByTestId } = render(<Status value={statusWithoutIcons} icon={false} />);

        // Check if the avatar has the initial of the status (W)
        const avatar = getByTestId("Avatar");
        expect(avatar).toHaveTextContent("W");
    });

    it("renders the correct icon when icon is true", () => {
        const statusWithIcons: StatusType = { status: "success", message: "Operation successful" };

        const { getByTestId } = render(<Status value={statusWithIcons} icon={true} />);

        // Check if the Avatar element contains the icon (CheckCircleIcon for success status)
        const avatar = getByTestId("Avatar");

        // Check if the avatar contains the appropriate icon, in this case CheckCircleIcon
        // Since CheckCircleIcon is rendered as part of the Avatar, we can check for its presence by looking for SVGs or icon classes
        const icon = avatar.querySelector("svg");
        expect(icon).toBeInTheDocument();  // The icon should be present inside the Avatar
    });
});
