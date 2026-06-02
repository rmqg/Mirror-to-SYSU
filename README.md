# Mirror-to-SYSU

自动向中山大学代码托管服务同步你的个人账户下的所有仓库。

Automatically synchronize all repositories under your personal account to the Sun Yat-sen University code hosting service.

该仓库设计为一个中枢控制型仓库，实现以下功能：

- 利用 GitHub Actions 向 git.sysu.edu.cn 推送个人账户下最近的至多 100 个仓库；
- 实现向 SYSU GitLab 注入 CI 使得即使在 GitLab 上提交更改也可向 GitHub 同步。

## 使用方法

1. 复刻本仓库至你的个人账户；
2. 准备以下令牌/密钥：
3. 在你复刻的 GitHub 本仓库 - Settings 中配置以下密钥：
4. 前往 GitHub Actions 手动发起一次同步：
