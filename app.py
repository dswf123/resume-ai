import streamlit as st
from dashscope import Generation
import os

# 从 streamlit secrets 读取密钥，不在代码里明文放
os.environ["DASHSCOPE_API_KEY"] = st.secrets["DASHSCOPE_API_KEY"]

st.title("✨ AI 简历优化大师")
st.write("粘贴你的经历，AI 帮你改成大厂范儿！")

original = st.text_area("📝 原始经历", height=200, placeholder="例如：负责客服，每天回消息...")
target = st.text_input("🎯 目标职位", placeholder="例如：高级运营经理")

if st.button("🚀 一键优化"):
    if not original or not target:
        st.warning("请填写内容！")
    else:
        with st.spinner("AI 正在思考..."):
            res = Generation.call(
                model="qwen-turbo",
                messages=[
                    {"role": "user",
                     "content": f"请作为资深HR，用STAR法则优化以下简历，目标是{target}：\n{original}"}
                ]
            )
            if res.status_code == 200:
                st.success("✅ 优化完成！")
                st.markdown(res.output.choices[0].message.content)
            else:
                st.error(f"出错了: {res.message}")