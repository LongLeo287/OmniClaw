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
import { useDynamicProperty } from "taipy-gui";

interface CaptionProps {
    text: string;
    defaultText: string;
    logoPath: string;
}

const styles = {
    container: {
        display: "flex",
        alignItems: "center",
    },
    logo: {
        width: "4em",
        height: "4em",
        marginRight: "10px",
    },
};

const LogoWithText = ({ text, defaultText, logoPath }: CaptionProps) => {
    const value = useDynamicProperty(text, defaultText, "");

    return (
        <div style={styles.container}>
            <img
                src={`data:image/png;base64,${logoPath}`}
                alt="LogoWithText"
                style={styles.logo}
            />
            <div>{value}</div>
        </div>
    );
};

export default LogoWithText;
