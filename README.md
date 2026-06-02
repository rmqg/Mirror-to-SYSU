# Mirror-to-SYSU

自动向中山大学代码托管服务同步你的个人账户下的所有仓库。

Automatically synchronize all repositories under your personal account to the Sun Yat-sen University code hosting service.

## 使用方法

1. 复刻本仓库至您的个人账户；
2. 请分别前往以下页面获取所需的令牌：
   1. [New fine-grained personal access token - GitHub](https://github.com/settings/personal-access-tokens/new)

      必要的权限：
      - Repository access: All repositories
      - Permissions：Contents - Read and write
      
      该令牌记为 `GHP_TOKEN_CUSTOM`
      
   2. [个人访问令牌·用户设置·中山大学代码托管服务](https://git.sysu.edu.cn/-/user_settings/personal_access_tokens)

      必要的权限：api, read_repository, write_repository
   
      该令牌记为 `GITLAB_TOKEN`

3. 在你复刻的 GitHub 本仓库 - Settings - Secrets and variables - Actions 中配置以下 Repository secrets：
   - `GHP_TOKEN_CUSTOM`
   - `GHP_USERNAME`：您的 GitHub 账户名（注意不是昵称，可参考本人主页 URL）
   - `GITLAB_TOKEN`
   - `GITLAB_USERNAME`：您在中山大学代码托管服务上的用户名（注意不是昵称，是您设置的个人账户命名空间，可参考本人主页 URL）
4. 前往 Actions 页面可尝试手动发起一次同步，也可等待每 4 小时自动触发一次。

## 实现效果

- 每个 4 小时，GitHub 仓库上发生的更改向中山大学代码托管服务同步；
- 即使存在新仓库，也能在中山大学代码托管服务同步创建；
- 调用 API 设置使得这些仓库能够直接利用镜像仓库机制，将中山大学代码托管服务上的更改同步到 GitHub 上；
- 理论上，你可以向任一平台进行提交操作，它们能够实现双向同步。

## 注意事项

- 建议您在 GitHub 上完成新仓库的创建操作，然后再向任一平台提交代码更改。作者未将该情况纳入考虑范围。
- 请注意保护您的令牌密钥等，不要在公共仓库中硬编码它们，也不要为它们分配过高的权限，以免造成不必要的损失。
- 您在中山大学代码托管服务上存储的内容应当遵循中华人民共和国以及中山大学的所有适用的规定，请勿同步违规内容。
- 为保护隐私，由 GitHub Actions 在中山大学代码托管服务首次创建的仓库默认处于私有状态，你必须手动检查它们并确认是否想要公开。
- 请合理使用中山大学代码托管服务。