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

import React, { MouseEvent, ReactNode, useEffect, useMemo, useRef } from "react";
import Chip from "@mui/material/Chip";
import Avatar from "@mui/material/Avatar";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import WarningIcon from "@mui/icons-material/Warning";
import ErrorIcon from "@mui/icons-material/Error";
import InfoIcon from "@mui/icons-material/Info";

import { getInitials } from "../../utils";
import { TaipyBaseProps } from "./utils";
import { useClassNames } from "../../utils/hooks";

export interface StatusType {
    status: string;
    message: string;
}

interface StatusProps extends TaipyBaseProps {
    value: StatusType;
    onClose?: (evt: MouseEvent) => void;
    openedIcon?: ReactNode;
    icon ?: boolean | string;
}

const status2Color = (status: string): "error" | "info" | "success" | "warning" => {
    status = (status || "").toLowerCase();
    status = status.length == 0 ? " " : status.charAt(0);
    switch (status) {
        case "s":
            return "success";
        case "w":
            return "warning";
        case "e":
            return "error";
    }
    return "info";
};

// Function to get the appropriate icon based on the status
const getStatusIcon = (status: string, icon?: boolean): ReactNode => {
    // Use useMemo to memoize the iconProps as well
    const color = status2Color(status);

    // Memoize the iconProps
    const iconProps = {
        sx: { fontSize: 20, color: `${color}.main` },
    };

    if (icon) {
        switch (color) {
            case "success":
                return <CheckCircleIcon {...iconProps} />;
            case "warning":
                return <WarningIcon {...iconProps} />;
            case "error":
                return <ErrorIcon {...iconProps} />;
            default:
                return <InfoIcon {...iconProps} />;
        }
    } else {
        return getInitials(status);
    }
};

const chipSx = { alignSelf: "flex-start" };

const defaultAvatarStyle = {
    width: "100%",
    height: "100%",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
};

const defaultAvatarSx = {
    bgcolor: "transparent",
};

const baseStyles = {
    fontSize: "1rem",
    textShadow: "1px 1px 4px black, -1px -1px 4px black",
};

const isSvgUrl = (icon: boolean | string) =>
    typeof icon === "string" && icon.substring(icon?.length - 4).toLowerCase() === ".svg"; // Check if it ends with ".svg"

const isInlineSvg = (icon: boolean | string) =>
    typeof icon === "string" && icon.substring(0, 4).toLowerCase() === "<svg"; // Check if the content starts with "<svg"

const Status = (props: StatusProps) => {
    const { value, id, icon = false } = props;
    const svgRef = useRef<HTMLDivElement>(null);
    const className = useClassNames(props.libClassName, props.dynamicClassName, props.className);

    useEffect(() => {
        if (typeof icon === "string" && svgRef.current) {
            svgRef.current.innerHTML = icon;
        }
    }, [icon]);

    const chipProps = useMemo(() => {
        const cp: Record<string, unknown> = {};
        const statusColor = status2Color(value.status);
        cp.color = statusColor;

        if (isSvgUrl(icon)) {
            cp.avatar = <Avatar src={icon as string} data-testid="Avatar" />;
        } else if (isInlineSvg(icon)) {
            cp.avatar = (
                <Avatar sx={defaultAvatarSx} data-testid="Avatar">
                    <div ref={svgRef} style={defaultAvatarStyle} />
                </Avatar>
            );
        } else {
            const isIcon = typeof icon === "boolean" && icon;
            cp.avatar = (
                <Avatar
                    sx={{
                        bgcolor: isIcon ? "transparent" : `${statusColor}.main`,
                        color: `${statusColor}.contrastText`,
                        ...baseStyles,
                    }}
                    data-testid="Avatar"
                >
                    {getStatusIcon(value.status, isIcon)}
                </Avatar>
            );
        }

        if (props.onClose) {
            cp.onDelete = props.onClose;
        }
        if (props.openedIcon) {
            cp.deleteIcon = props.openedIcon;
        }
        return cp;
    }, [value.status, props.onClose, props.openedIcon, icon]);

    return <Chip id={id} variant="outlined" {...chipProps} label={value.message} sx={chipSx} className={className} />;
};

export default Status;
