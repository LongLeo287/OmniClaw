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

import React, { useMemo } from "react";
import { LoV, useLovListMemo } from "taipy-gui";

interface VisualLabelListProps {
    lov?: LoV;
    defaultLov?: string;
    sort?: "asc" | "desc";
}

const styles = {
    listItem: {
        display: "flex",
        alignItems: "center",
    },
    image: {
        marginRight: "8px",
        width: "1em",
        height: "1em",
    },
};

const VisualLabelList: React.FC<VisualLabelListProps> = ({ lov, defaultLov = "", sort }) => {
    const lovList = useLovListMemo(lov, defaultLov);

    const sortedLovList = useMemo(() => {
        if (sort) {
            return lovList.slice().sort((a, b) => {
                return sort === "asc" ? a.id.localeCompare(b.id) : b.id.localeCompare(a.id);
            });
        }
        return lovList;
    }, [lovList, sort]);

    return (
        <div>
            <ul>
                {sortedLovList.map((item, index) => (
                    <li key={index} style={styles.listItem}>
                        {typeof item.item === "string" ? null : (
                            <img src={item.item.path} alt={item.item.text} style={styles.image} />
                        )}
                        {item.id}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default VisualLabelList;
